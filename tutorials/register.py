from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['POST'])
def signup(request, pk):
    if request.method == 'POST':
        register_data = JSONParser().parse(request)
        username = register_data["username"]
        raw_password = register_data["password"] 
        user = authenticate(username = username, password = raw_password) 
        print('Usuario: '+ user)       
    else:
     
      print('Error')

