from django.db import models
from .forms import User


class News(models.Model):
    headline = models.CharField(max_length=1024)
    original_link = models.CharField(max_length=2048)
    img_link = models.CharField(max_length=2048)
    newspaper_name = models.CharField(max_length=255)
    bookmark = models.ManyToManyField(User, related_name='bookmark', blank=True)


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    
    def __str__(self):
        return self.title