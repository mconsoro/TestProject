from django.urls import path
from account import views

urlpatterns = [ 
    #url(r'^api/account$', views.login),
    path('api/account/', views.LoginView.as_view())
]
