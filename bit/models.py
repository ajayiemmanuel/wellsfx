from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200, null = True)
    phone = models.CharField (max_length = 200, null = True)
    email = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "oohhi.png", null = True, blank = True)
    date_created = models.DateTimeField (auto_now_add = True, null = True)

    def __str__(self):
        return self.name



