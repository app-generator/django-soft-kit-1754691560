# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    status = models.TextField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Apikey(models.Model):

    #__Apikey_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    key = models.TextField(max_length=255, null=True, blank=True)
    expire = models.DateTimeField(blank=True, null=True, default=timezone.now)
    hash = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Apikey_FIELDS__END

    class Meta:
        verbose_name        = _("Apikey")
        verbose_name_plural = _("Apikey")



#__MODELS__END
