from django.urls import path
from .views import *
app_name = 'user'

urlpatterns = [
    path("signup/", signupuser, name='signupuser'),
    path('logout', logoutuser, name= 'logoutuser'),
    path('login', loginuser, name= 'loginuser'),
]