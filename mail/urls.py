from django.urls import path
from .views import *

urlpatterns = [
     path('', mail, name="mail"),
]