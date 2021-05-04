from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.latest, name='latest'),
    path('archive', views.archive, name='archive')
]
