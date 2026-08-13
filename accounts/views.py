from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import logout
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

def logout_view(request):
    logout(request)
    
    return redirect("home")
