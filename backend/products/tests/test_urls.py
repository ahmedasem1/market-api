from django.test import SimpleTestCase
from django.urls import resolve, reverse
from products.views import *


class TestUrls(SimpleTestCase):
    def test_product_list_is_resolved(self):
        url = reverse("product_list")
        self.assertEquals(resolve(url).func, product_list_create_view)

    def test_home_is_resolved(self):
        url = reverse("product_detail", args=["1"])
        self.assertEquals(resolve(url).func.view_class, ProductDetailAPIView)
