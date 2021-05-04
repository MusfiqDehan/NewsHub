from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest, name='latest')
]
