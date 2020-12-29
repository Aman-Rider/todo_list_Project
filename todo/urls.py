from django.urls import path
from .views import * 
app_name = 'todo'

urlpatterns = [
    path('', home, name='home'),
    path('currenttodos', currenttodos, name = 'currenttodos' )
]
