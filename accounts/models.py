# accounts/models.py
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    sex = models.CharField(max_length=255)


class Address(models.Model):
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=8)

    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="addresses"
    )
