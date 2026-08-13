from django.urls import path
from .views import *

urlpatterns = [
    path("test_profile", test_profile, name = "profile-test")
]