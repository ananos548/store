from cart.cart import Cart
from cart.forms import CartForm


def cart_detail(request):
    cart = Cart(request)
    for item in cart:  # Сделать отдельный файл logic и прописать в нём логику for
        item['update_quantity_form'] = CartForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )
