from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from posts.models import *

User = get_user_model()

@login_required
def my_profile(request):
    
    posts = Post.objects.filter(
        user = request.user
    ).order_by(
        "-created_at"
    )
    
    return render(
        request, 
        "profiles/profile.html",
        {
            "profile_user" : request.user,
            "posts" : posts,
        }
    )
    

def profile(request, username):
    user = get_object_or_404(
        User, 
        username=username
    )
    
    posts = Post.objects.filter(
        user = user
    ).order_by("-created_at")
    
    return render(
        request, 
        "profiles/profile.html",
        {
            "profile_user" : user,
            "posts" : posts,
        }
    )
    
    
 
