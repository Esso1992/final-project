# service/urls.py
from django.urls import path
from .routes import list_all_products, list_by_name, list_by_category, list_by_availability

urlpatterns = [
    # Your other URLs
    path('api/products/all/', list_all_products, name='list_all_products'),
    path('api/products/name/<str:name>/', list_by_name, name='list_by_name'),
    path('api/products/category/<str:category>/', list_by_category, name='list_by_category'),
    path('api/products/availability/<str:availability>/', list_by_availability, name='list_by_availability'),
]

