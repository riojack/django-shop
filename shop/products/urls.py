from django.urls import path

from .views.add_products import AddProductsView
from .views.search_products import SearchProductsView

urlpatterns = [
    path('', AddProductsView.as_view(), name='manage products'),
    path('search', SearchProductsView.as_view(), name='search products'),
]
