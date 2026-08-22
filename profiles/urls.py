from django.urls import path
from .views import *

urlpatterns = [
    path("", my_profile, name="my_profile"),
    path("<str:username>/", profile, name = "profile"),
]