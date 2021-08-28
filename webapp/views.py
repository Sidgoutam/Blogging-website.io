from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Stories
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages 

def index(request):
    return render(request=request,
                  template_name = "main/home.html",
                  context ={"stories":Stories.objects.all})

def Night(request):
    return render(request=request,
                  template_name = "main/storydeets/Night.html",
                  context ={"stories":Stories.objects.all})

def He(request):
    return render(request=request,
                  template_name = "main/storydeets/He.html",
                  context ={"stories":Stories.objects.all})

def Faith(request):
    return render(request=request,
                  template_name = "main/storydeets/Faith.html",
                  context ={"stories":Stories.objects.all})

def register(request):
    form = UserCreationForm
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created : {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("webapp:index")
        else :
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
                
    
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesfully !")
    return redirect("webapp:index")

def login_request(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("webapp:index")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request,
                "main/login.html",
                context={"form":form})
