
from django.db import models

class CertificateRequest(models.Model):
    server_ip = models.GenericIPAddressField()
    device_type = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255,unique=True)  
    model_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    device_id = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.customer_name  



class PersonCertificate(models.Model):
    server_ip = models.CharField(max_length=255) 
    person_name = models.CharField(max_length=255, unique=True)
    project_name = models.CharField(max_length=255)

    PROJECT_SCOPE_CHOICES = [
        ('internal', 'Internal'),
        ('external', 'External'),
    ]
    project_scope = models.CharField(max_length=10, choices=PROJECT_SCOPE_CHOICES, default='internal')

    def __str__(self):
        return self.person_name


  




