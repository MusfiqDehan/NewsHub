from django.test import TestCase, Client
from django.urls import reverse
from news.models import News
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse("news:register")
        self.login_url = reverse("news:login")


    def test_register_POST(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "news/register.html")


    def test_login_POST(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "news/login.html")

