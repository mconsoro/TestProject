from django.urls import path
from account import views



urlpatterns = [ 
   
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('admin/', views.Admin.as_view(), name ='admin')
]
