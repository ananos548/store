from django.urls import path
from .views import *


urlpatterns = [
    path('cart', CartListView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>', cart_remove_all, name='cart_remove_all'),
    path('cart/remove_piece/<int:product_id>', cart_remove_few, name='cart_remove_few'),
]
