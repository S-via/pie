# Django needs to know which URL should trigger this view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
