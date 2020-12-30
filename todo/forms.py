from django.forms import ModelForm
from .models import Todo_list
class TodoForm(ModelForm):
    class Meta:
        model = Todo_list
        fields = ['title', 'memo', 'important']