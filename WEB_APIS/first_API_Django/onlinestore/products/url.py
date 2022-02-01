from django.urls import path
# ProductDetailView, ProductListView
from .views import manufacturer_detail, manufacturer_list, product_detail, product_list


urlpatterns = [
    # path("", ProductListView.as_view(),name="products_list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(),name="products_details")

    path("products", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-details"),
    path("manufacturer", manufacturer_list, name="manufacturer-list"),
    path("manufacturer/<int:pk>", manufacturer_detail, name="manufacturer-detail"),



]
