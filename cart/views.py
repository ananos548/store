from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseFormView
from django.http import HttpResponse

from store.models import Product
from cart.cart import Cart
from .forms import CartForm


class CartListView(ListView, BaseFormView):
    template_name = 'cart/detail.html'
    model = Product
    form_class = CartForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        if cd['quantity'] > product.quantity:
            raise ValidationError('Вы добавили слишком много единиц товара')
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove_few(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_some(product)
    return redirect('cart_detail')


def cart_remove_all(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
