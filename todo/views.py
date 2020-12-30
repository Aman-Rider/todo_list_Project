from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo_list
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#Create your views here.
def home(request):
    return render(request, 'todo/home.html')

@login_required
def currenttodos(request):
    alltodos = Todo_list.objects.filter(user = request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos':alltodos})

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todo:currenttodos')
        except ValueError:
             return render(request, 'user/createtodo.html', {'form':TodoForm(), 'error':'Invalid Data Passed. Try again!'})        

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo_list, pk = todo_pk, user = request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo:currenttodos')
        except ValueError:
             return render(request, 'user/viewtodo.html', {'form':TodoForm(), 'error':'Invalid Data Passed. Try again!'})       
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo_list, pk = todo_pk, user = request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('todo:currenttodos')
    
@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo_list, pk = todo_pk, user = request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:currenttodos')


@login_required
def completedtodo(request):
    alltodos = Todo_list.objects.filter(user = request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodo.html', {'todos':alltodos})
