from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail

from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

# from rest_framework.authtoken.models import Token

# @api_view(['POST'])
# def register(request):
#    user_data  = JSONParser().parse(request)
        
#    user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
#    user.first_name = user_data["first_name"]
#    user.last_name = user_data["last_name"]
#    user.is_active = user_data["is_active"]
#    user.save()

@api_view(['POST'])
def signup(request):
 
     register_data = JSONParser().parse(request)
     username = register_data["username"]
     password = register_data["password"] 
     user = authenticate(username = username, password = password)
     print(str(user))
   #   if not user:
   #      print("No user")
   #   if not user.check_password(password):
   #       print("No password")
   #   if not user.is_active:
   #       print("User no active")
     if not user.is_authenticated:
         print("User no autenticado")
     if user.is_authenticated:

       #print("Se ha autenticado: "+ str(user.is_authenticated))  

       send_mail(
          'Correo de prueba',
          'Esto es un correo de pruebas.',
          'miguelconsoro@gmail.com',
          ['miguelconso29@gmail.com'],
          fail_silently=False)

              
     return JsonResponse(user, safe=False)
#   except:
#       print("Error")
#       return JsonResponse(register_data, status=status.HTTP_204_NO_CONTENT)
      

