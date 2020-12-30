from django.urls import path
from .views import * 
app_name = 'todo'

urlpatterns = [
    path('', home, name='home'),
    path('currenttodos', currenttodos, name = 'currenttodos' ),
    path('createtodo', createtodo, name = 'createtodo'),
    path('completedtodo', completedtodo, name = 'completedtodos'),
    path('viewtodo/<int:todo_pk>', viewtodo, name = 'viewtodo'),
    path('viewtodo/<int:todo_pk>/complete', completetodo, name = 'completetodo'),
    path('viewtodo/<int:todo_pk>/delete', deletetodo, name = 'deletetodo')
]
