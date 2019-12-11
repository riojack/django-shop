from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_product, name='manage products'),
    path('search', views.search_products, name='search products'),
]
