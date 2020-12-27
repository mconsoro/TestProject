from rest_framework import serializers

class LogoutSerializer(serializers.Serializer):
   refresh = serializers.CharField()

   def validation(self, attr):
       self.token = attr['refresh']

       return attr
   def save(self, **kwargs):
       RefreshToken(self.token).backList()    