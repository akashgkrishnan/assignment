from django.urls import path
from . import views


urlpatterns = [
    path('service_home', views.home, name='service_home'),
    path('my_services', views.my_services, name='my_services'),
    path('requested-services', views.requested_service, name='requested-services'),
]