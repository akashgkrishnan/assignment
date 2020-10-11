from django.db import models
from django.contrib.auth.models import User

from client_user.models import client_user_details


class service_user_details(models.Model):
    user_info = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True)


    def __str__(self):
        return self.user_info

class service_offered(models.Model):
    service_name = models.CharField(max_length = 200)
    service_cost = models.PositiveIntegerField()
    service_description = models.TextField()
    user_name = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True)


    def __str__(self):
        return self.service_name

class service_booking_detail(models.Model):
    service_id = models.ForeignKey(service_offered, on_delete = models.DO_NOTHING)
    client_booked_for = models.ForeignKey(client_user_details, on_delete = models.DO_NOTHING)
    service_provider = models.ForeignKey(service_user_details, on_delete = models.DO_NOTHING)


    def __str__(self):
        return self.service_id.service_name