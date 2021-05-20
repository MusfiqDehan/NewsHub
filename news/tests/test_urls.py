from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import *


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse("news:register")
        self.assertEquals(resolve(url).func, registerPage)
    
    def test_login_url_resolves(self):
        url = reverse("news:login")
        self.assertEquals(resolve(url).func, loginPage)
    
    def test_logout_url_resolves(self):
        url = reverse("news:logout")
        self.assertEquals(resolve(url).func, logoutUser)

    def test_bookmark_url_resolves(self):
        url = reverse("news:bookmark_list")
        self.assertEquals(resolve(url).func, bookmark_list)

    def test_latest_url_resolves(self):
        url = reverse("news:latest")
        self.assertEquals(resolve(url).func, latest)

    def test_archive_url_resolves(self):
        url = reverse("news:archive")
        self.assertEquals(resolve(url).func, archive)