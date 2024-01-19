# service/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/all/', ProductViewSet.as_view({'get': 'list_all_products'}), name='list_all_products'),
    path('api/products/name/<str:name>/', ProductViewSet.as_view({'get': 'list_by_name'}), name='list_by_name'),
    path('api/products/category/<str:category>/', ProductViewSet.as_view({'get': 'list_by_category'}), name='list_by_category'),
    path('api/products/availability/<str:availability>/', ProductViewSet.as_view({'get': 'list_by_availability'}), name='list_by_availability'),
]
