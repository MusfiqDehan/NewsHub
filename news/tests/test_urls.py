from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import *

class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        assert  1 == 2 