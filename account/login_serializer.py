from rest_framework import serializers 
from account.models import LoginInfo 
 
class LoginInfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = LoginInfo
        fields = ('first_name',
                  'last_name',
                  'is_authenticated')