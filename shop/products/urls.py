from django.urls import path

from .services.product_validator import ProductValidator
from .views.add_products import AddProductsView
from .views.search_products import SearchProductsView

urlpatterns = [
    path('', AddProductsView.as_view(validator=ProductValidator()), name='manage products'),
    path('search', SearchProductsView.as_view(), name='search products'),
]
