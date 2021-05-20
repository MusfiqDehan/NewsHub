from django.db import models
from django.urls import reverse
from .forms import User
from datetime import datetime

class News(models.Model):
    headline = models.CharField(max_length=1024)
    original_link = models.CharField(max_length=2048)
    img_link = models.CharField(max_length=2048)
    newspaper_name = models.CharField(max_length=255)
    bookmark = models.ManyToManyField(User, related_name='bookmark', blank=True)

    def get_absolute_url(self):        
        return reverse('news:archive')