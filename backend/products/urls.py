from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
    path('update/<int:pk>/', views.Product_detail, name='update_items'),


]
