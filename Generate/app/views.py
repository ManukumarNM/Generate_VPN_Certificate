import os
import subprocess
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CertificateRequest, PersonCertificate


"""Author: Manukumar N M"""
"""Code: VPN certificate creation code using Python and Django"""
"""It has server details and credentials make it secure in the server"""
@csrf_exempt
def generate_certificate(request, certificate_type):
    try:
        """Decode the coming data into the Unicode string from BYtestream"""
        data = json.loads(request.body.decode('utf-8'))
        server_ip = data.get('server_ip')
        
        if certificate_type == 'device':
            customer_name = f"{data.get('device_type')}_{data.get('site_id')}_{data.get('customer_name')}"
            certificate = CertificateRequest(
                server_ip=server_ip,
                device_id=data.get('device_id'),
                site_id=data.get('site_id'),
                device_type=data.get('device_type'),
                model_name=data.get('model_name'),
                customer_name=customer_name,
                project_type=data.get('project_type'),
            )
        elif certificate_type == 'person':
            person_name = f"{data.get('project_name')}_{data.get('person_name')}"
            certificate = PersonCertificate(
                server_ip=server_ip,
                person_name=person_name,
                project_name=data.get('project_name'),
            )
        else:
            return JsonResponse({'error': 'Invalid certificate type.'}, status=400)
        """ Save the data in the database - sqlite3.db"""
        certificate.save()
        """Environmental setup for the server to access not compulsory but sometimes it required"""
        os.environ['TERM'] = 'xterm'
        password = "********"

        remote_certificate_file_path = f'/root/certificate/{customer_name if certificate_type == "device" else person_name}.ovpn'
        command = f'sshpass -p {{password}} ssh root@{server_ip} "TERM=xterm /root/OpenVPN-Setup/new_openvpn-install.sh 1 {customer_name if certificate_type == "device" else person_name}"'
        
        """ Here we can subprocess or http response to get the executed script result"""
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            scp_command = f'sshpass -p password scp root@{server_ip}:{remote_certificate_file_path} .'
            scp_result = subprocess.run(scp_command, shell=True, stderr=subprocess.PIPE)
            
            if scp_result.returncode == 0:
                filename = f'{customer_name if certificate_type == "device" else person_name}.ovpn'
                
                with open(filename, 'rb') as ovpn_file:
                    ovpn_content = ovpn_file.read()
                
                response = HttpResponse(ovpn_content, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            else:
                return JsonResponse({'error': f'SCP command execution failed. Stderr: {scp_result.stderr.decode()}'}, status=500)
        else:
            return JsonResponse({'error': f'Command execution failed}' status=500)
    
    except Exception as e:
        return JsonResponse({'error': f'Internal server error},' status=500)


# Write a method to call the device and person certificate 
@csrf_exempt
def generate_device_certificate(request):
    return generate_certificate(request, 'device')

@csrf_exempt
def generate_person_certificate(request):
    return generate_certificate(request, 'person')
