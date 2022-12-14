from django.urls import path
from .views import *


urlpatterns = [
    path('', CartListView.as_view(), name='cart_detail'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart_remove_all, name='cart_remove_all'),
    path('remove_piece/<int:product_id>', cart_remove_few, name='cart_remove_few'),
]
