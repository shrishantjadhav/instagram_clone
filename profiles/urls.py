from django.urls import path
from .views import *

urlpatterns = [
    path("", my_profile, name="my_ profile"),
    path("<str:username>/", profile, name = "profile"),
]