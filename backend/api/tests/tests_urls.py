from django.test import SimpleTestCase
from django.urls import resolve, reverse
from api.views import *


class TestUrls(SimpleTestCase):
    def test_home_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, api_home)
