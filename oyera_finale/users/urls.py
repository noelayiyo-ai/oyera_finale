from django.urls import path
from .import views
from django.contrib.auth import views as auth_views 


   

url_patterns = [
    path('register/',views.registerPage, name="register"),
   # path('login/', views.loginPage, name="login"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'), 
    
]


