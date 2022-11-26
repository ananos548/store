from decimal import Decimal
from store_project import settings
from store.models import Product


class Cart(object):

    def __init__(self, request):
        """ Инициализация корзины """
        self.session = request.session  # Получаем текущую сессию
        cart = self.session.get(settings.CART_SESSION_ID)  # пытаемся получить корзину с текущей сессии
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()  # Сохраняем корзину в сессии

    def save(self):
        """ сохраняет все изменения в корзине в сессии и помечает сессию как modified  """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True  # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен

    def remove_some(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= 1
            self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """ Перебор элементов в корзине и получение продуктов из базы данных """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item  # yield возвращает генератор

    def __len__(self):
        """ Кол-во товаров в корзине """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
