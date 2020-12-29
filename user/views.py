from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password = password1)
                user.save()
                login(request, user)
                return redirect('todo:currenttodos')
            except IntegrityError:
                return render(request, 'user/signup.html', {'form':UserCreationForm(), 'error':'Username already taken'})
        else:
            return render(request, 'user/signup.html', {'form':UserCreationForm(), 'error':'Passwords do not match'})
        print(username)
        return redirect('todo:home')
    else:
        return render(request, 'user/signup.html', {'form':UserCreationForm()})

def logoutuser(Request):
    logout(Request)
    return redirect('todo:home')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('todo:home')
        else:
            return render(request, 'user/signin.html', {'form':AuthenticationForm(), 'error':'Invalid Credentials'})        
        return redirect('todo:home')
    else:
        return render(request, 'user/signin.html', {'form':AuthenticationForm()})