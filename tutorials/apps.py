from django.apps import AppConfig

from rest_framework.permissions import IsAuthenticated


class TutorialsConfig(AppConfig):    
    name = 'tutorials'
    permission_classes = [IsAuthenticated]

 
