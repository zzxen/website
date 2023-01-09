from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import News , PricePanel
from . import forms



# Create your views here.

def homepage(request):
    return render(request , "index.html")

def registerform(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = forms.RegisterForm()
    return render(request , "register.html" , context = {"form" : form})

def loginform(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"] , password = form.cleaned_data["password"])
            if user is not None:
                if user.is_active:
                    login(request , user)
                    return redirect("home")
                else:
                    return redirect("ban")
            else:
                return redirect("ban")
    return render(request , "login.html" , context = {"form" : form})

def logoutform(request):
    logout(request)
    return redirect("home")

def pricepanel(request):
    price = PricePanel.objects.all()
    return render(request , "price.html" , {"form" : price})

def banned(request):
    return render(request , "ban.html")

def newssection(request):
    form = News.objects.all()
    return render(request , 'news.html' , context = {"news" : form})