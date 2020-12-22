from .utils import token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse

class AppActivateUrl:
    def __init__(self, pk, request, user):
         self.pk = pk
         self.request = request
         self.user = user

    def createUrl(self):
        try:
          print("entro")
          uidb64 = force_bytes(urlsafe_base64_encode(self.pk))
          domain = get_current_site(self.request).domain
          link = reverse('activate', kwargs = {'uidb64': uidb64, 
                         'token': token_generator.make_token(self.user)})
          url = 'http://' + domain + link
          return url
        except:
            return "Error"  
