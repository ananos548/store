from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ListMainView.as_view(), name='index'),
    path('products', ListProductsView.as_view(), name='products'),
    path('products/cat/<str:code>', ListCategoryView.as_view(), name='category'),
    path('products/<int:pk>', DetailProductView.as_view(), name='product_detail'),
    path('search', SearchView.as_view(), name='search'),

]
