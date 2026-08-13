from django.shortcuts import render
from django.http import HttpResponse

def test_profile(request):
    return HttpResponse("Profiles app is working!")
