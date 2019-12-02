from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.user.username


