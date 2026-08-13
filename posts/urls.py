from django.urls import path
from .views import *

urlpatterns = [
    path("test_post/", test_post, name = "post-test")
]