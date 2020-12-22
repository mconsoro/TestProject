from rest_framework import serializers
from django.db import models

class LoginInfo(models.Model):
    first_name ="" 
    last_name = ""
    is_authenticated = False
    