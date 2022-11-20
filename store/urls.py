from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('products/cat/<str:code>', ListCategoryView.as_view(), name='category'),
    path('products/<int:pk>', DetailProductView.as_view(), name='product_detail'),


]
