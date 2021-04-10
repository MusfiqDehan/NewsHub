from django.http import HttpResponse
from django.shortcuts import render

app_name = 'news'

def index(request):
    return render(request, 'news/index.html')