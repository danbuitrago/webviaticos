from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login as auth_login    #crear la cookie
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .forms import SolicitudForm

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
                auth_login(request,user)
                return redirect('vistasol')
            
            except IntegrityError:
                return render(request, 'registration/signup.html/', {"form": UserCreationForm, "error": "Username already exists."})
    return render(request, 'registration/signup.html/', {"form": UserCreationForm, "error": "Passwords did not match."})
 
def login(request):
    if request.method == 'GET':
        return render (request, 'login.html',{'form':AuthenticationForm})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form':AuthenticationForm, 'error':'Username or password incorrect'})  
        else:
            auth_login(request,user)
            return redirect('vistasol')

@login_required
def vistasol(request):
    return render(request, 'vistasol.html')
@login_required
def vistacom(request):
    return render(request, 'vistacom.html')
@login_required
def crearsol(request):
    if request.method=='GET':
        return render (request, 'crearsol.html',{'form':SolicitudForm})
    else:
        form=SolicitudForm(request.POST)
        nuevasol=form.save(commit=False)
        nuevasol.user=request.user
        nuevasol.save()
        return redirect('vistasol')

def crearcom(request):
    return render(request, 'crearcom.html')

def signout(request):
    logout(request)
    return render(request, 'login.html')
@login_required
def base(request):
    return render(request, 'base.html')