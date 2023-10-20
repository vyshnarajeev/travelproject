from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place
# Create your views here.



def about(request):
    return render(request,"about.html")

def index(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})



def services(request):
    return render(request,"destinations.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['firstName']
        lastname = request.POST['secondName']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['conform password']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)

                user.save();
                return redirect('login')


        else:
            messages.info(request, "Password not matching")
            return redirect('register')

    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')
    return render(request, "login.html")