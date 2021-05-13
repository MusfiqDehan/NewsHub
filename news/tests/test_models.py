from django.test import TestCase, Client
from django.urls import reverse
from news.models import Headline, News


class TestModels(TestCase):

    def setUp(self):
        self.news1 = News.objects.create(
            headline = 'head line',
            original_link = 'original link',
            img_link = 'image link',
            newspaper_name = 'newspaper name'
        )