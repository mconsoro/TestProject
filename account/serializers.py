from rest_framework import serializers 
from django.contrib.auth.models import User
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('password','is_superuser','username','first_name',
                  'last_name','email','is_staff','is_active')
                  