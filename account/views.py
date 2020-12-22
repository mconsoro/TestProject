from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as do_logout

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .send_mail_c import AppSenEmail
from .create_activate_url import AppActivateUrl
from .models import LoginInfo
from .serializer import LoginInfoSerializer

# @api_view(['POST'])
# def register(request):
#    user_data  = JSONParser().parse(request)

#    user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
#    user.first_name = user_data["first_name"]
#    user.last_name = user_data["last_name"]
#    user.is_active = False
#    user.save()

@api_view(['POST','GET'])
def login(request):
  login_info_json = "{message: 'error'}"
  if request.method == 'GET':
    do_logout(request)
    print('logout')

  else:

    if request.user.is_authenticated:
       print(str(request)) 
    else:  
  #try:
      register_data = JSONParser().parse(request)      
      username = register_data["username"]
      password = register_data["password"]
      user = authenticate(username = username, password = password)
  #   if not user:
   #      print("No user")
   #   if not user.check_password(password):
   #       print("No password")
      print(str(request.user.is_authenticated))
      if not user.is_active:
        
        # act_obj = AppActivateUrl(user.pk, request, user)
        # register_data['activate_rul'] = act_obj.createUrl()
        # register_data['to'] = user.email
        
        #AppSenEmail(register_data).send_m()

        print("User no active")
      if not user.is_authenticated:
        print("User no autenticado")
      if user.is_authenticated:
        print("Se ha autenticado: "+ str(user.is_authenticated))
      
      LoginInfo.first_name = user.first_name
      LoginInfo.last_name = user.last_name
      LoginInfo.is_authenticated = user.is_authenticated
        
      login_info_serializer = LoginInfoSerializer(LoginInfo)   
      #print(login_info_serializer.data)
  return JsonResponse(login_info_serializer.data, safe=False)
#   except:
#       print("Error")
#       return JsonResponse(register_data, status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def logout(request):

#      do_logout(request)
#      print('logout')
#      return JsonResponse('{test:"Sessinón cerrada"}', safe=False)
