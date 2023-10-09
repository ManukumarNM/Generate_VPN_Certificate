
# from django.urls import path
# from . import views

# urlpatterns = [
#     # Other URL patterns...
#     path('generate_ovpn/', views.generate_ovpn_certificate, name='generate_ovpn_certificate'),
#     path('generate_person/', views.generate_person_certificate, name='generate_person_certificate'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/device/', views.generate_device_certificate, name='generate_device_certificate'),
    path('generate_certificate/person/', views.generate_person_certificate, name='generate_person_certificate'),
]
