# join_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.add_contact, name='add_contact'),
]
