from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=1024)
    original_link = models.CharField(max_length=2048)
    newspaper_name = models.CharField(max_length=255)
    img_link = models.CharField(max_length=2048)