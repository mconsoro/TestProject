from django.conf.urls import url
from account import views

urlpatterns = [ 
    #url(r'^api/account$', views.register),
    url(r'^api/account$', views.signup)
]