from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
