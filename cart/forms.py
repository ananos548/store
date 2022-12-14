# Чтобы добавить элементы в корзину, нам нужна форма, позволяющая пользователю выбрать количество добавляемого товара.
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from store.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(label='', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)