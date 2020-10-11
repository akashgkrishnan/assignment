from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User



class client_user_details(models.Model):
    user_info = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True)


    def __str__(self):
        return self.user_info
