from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login     #crear la cookie

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html/',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()                
                login(request, user)
                return redirect('vistasol')
            
            except IntegrityError:
                return render(request, 'registration/signup.html/', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registration/signup.html/', {"form": UserCreationForm, "error": "Passwords did not match."})
   
def login(request):
    return render(request, 'login.html')

#@login_required
def vistasol(request):
    return render(request, 'vistasol.html')

def vistacom(request):
    return render(request, 'vistacom.html')

def crearsol(request):
    return render(request, 'crearsol.html')

def crearcom(request):
    return render(request, 'crearcom.html')