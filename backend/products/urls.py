from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list_create_view, name="product_list"),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
