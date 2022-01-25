from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels


class Profile(AbstractUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    birth_day = jmodels.jDateField(null=True, blank=True)
    terms_and_conditions = models.BooleanField(default=False)
    password = models.CharField(max_length=256)


