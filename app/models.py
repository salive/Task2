from django.db import models


class UserInfo(models.Model):
    name = models.CharField('Name', max_length=200, null=False)
    phone_number = models.CharField('Phone number', max_length=20, null=False)
