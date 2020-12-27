from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as do_logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser

from .send_mail_c import AppSenEmail
from .create_activate_url import AppActivateUrl
from .serializer import UserSerializer
import jwt
# @api_view(['POST'])
# def register(request):
#    user_data  = JSONParser().parse(request)

#    user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
#    user.first_name = user_data["first_name"]
#    user.last_name = user_data["last_name"]
#    user.is_active = False
#    user.save()

# @api_view(['POST','GET'])
# def login(request):
#   login_info_json = "{message: 'error'}"
#   if request.method == 'GET':
#     do_logout(request)
#     print('logout')

#   else:

#     if request.user.is_authenticated:
#        print(str(request)) 
#     else:  
#   #try:
#       register_data = JSONParser().parse(request)      
#       username = register_data["username"]
#       password = register_data["password"]
#       user = authenticate(username = username, password = password)
#   #   if not user:
#    #      print("No user")
#    #   if not user.check_password(password):
#    #       print("No password")
#       print(str(request.user.is_authenticated))
#       if not user.is_active:
        
#         # act_obj = AppActivateUrl(user.pk, request, user)
#         # register_data['activate_rul'] = act_obj.createUrl()
#         # register_data['to'] = user.email
        
#         #AppSenEmail(register_data).send_m()

#         print("User no active")
#       if not user.is_authenticated:
#         print("User no autenticado")
#       if user.is_authenticated:
#         print("Se ha autenticado: "+ str(user.is_authenticated))
      
#       LoginInfo.first_name = user.first_name
#       LoginInfo.last_name = user.last_name
#       LoginInfo.is_authenticated = user.is_authenticated
        
#       login_info_serializer = LoginInfoSerializer(LoginInfo)   
#       #print(login_info_serializer.data)
#   return JsonResponse(login_info_serializer.data, safe=False)
#   except:
#       print("Error")
#       return JsonResponse(register_data, status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def logout(request):

#      do_logout(request)
#      print('logout')
#      return JsonResponse('{test:"Sessinón cerrada"}', safe=False)


class LoginView(GenericAPIView):
   def post(self, request):
    
       data = request.data 
       user_name = data.get('username')
       password = data.get('password')
       user = authenticate(username = user_name, password = password)
      
       if user:
           auth_token = jwt.encode({'username': user.username }, 'mc29')
           
           serializer = UserSerializer(user)
           
           data = {"user": serializer.data,'token': auth_token }
           
           return Response(data, status = status.HTTP_200_OK)

       return Response({'detail':'Ivalid credentials'}, status = status.HTTP_400_BAD_REQUEST)
    

class Admin(GenericAPIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
       
       try:
         return Response({'Restult: Ok'},status = status.HTTP_200_OK)
       except:
         return Response({'Restult: Error'},status = status.HTTP_400_BAD_REQUEST)



