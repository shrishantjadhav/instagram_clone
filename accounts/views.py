from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(
                request, 
                "Account created successfully!"
            )
        
            return redirect('login')
            
    else:
        form = SignupForm()
        
    return render(request, "accounts/signup.html", {"form" : form})

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            next_url = request.GET.get("next")
            
            if next_url: 
                return redirect(next_url)
            
            return redirect('home')
    
    else: 
        form = AuthenticationForm()
        
    return render(request, "accounts/login.html", {"form" : form})

def logout_view(request):
    logout(request)
    
    return redirect("home")
