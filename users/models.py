from __future__ import unicode_literals
import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('profile', str(instance.id), filename)

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="user_profile_user",
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        _("First Name"),
        max_length=128,
        db_index=True)

    last_name = models.CharField(
        _("Last Name"),
        max_length=128,
        null=True,
        blank=True,
        db_index=True)

    profile_picture = models.ImageField(
        upload_to=get_image_path, blank=True)

    i_can = models.CharField(
        max_length=200,
        blank=False)

    i_need = models.CharField(
        max_length=200,
        blank=False)

    verified = models.BooleanField(
        default=False)
    
    def __str__(self):
        return self.user.username