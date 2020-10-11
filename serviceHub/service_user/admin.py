from django.contrib import admin
from .models import service_offered, service_user_details, service_booking_detail

# Register your models here.
admin.site.register(service_offered)
admin.site.register(service_user_details)
admin.site.register(service_booking_detail)