from django.http import JsonResponse
from .models import Manufacturer, Product


def product_list(request):
    products = Product.objects.all() # [:30]
    data = {"products": list(products.values())}  # "pk", "name"
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name ": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping,
            "quantity": product.quanties
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product now found"
            }},
            status=404)
    return response


def manufacturer_list(request):
    manufacturer = Manufacturer.objects.filter(active=True) 
    data = {"manufacturers": list(manufacturer.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_product = manufacturer.products.all()
        data = {"manufacture": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "product": list(manufacturer_product.values())
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer does not exist"
            }}, status=404)
    return response

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_details.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
