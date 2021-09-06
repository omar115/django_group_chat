from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage),
    path('room/',roomview, name='room')
]