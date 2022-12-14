from django.db.models import Q
from django.http import Http404
from django.views.generic.edit import BaseFormView

from cart.forms import CartForm
from .models import Category, Product
from django.views.generic import ListView, DetailView


class ListMainView(ListView):
    template_name = 'store/index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListMainView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CartFormView(BaseFormView):
    form_class = CartForm


class ListProductsView(CartFormView, ListView):
    template_name = 'store/products.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProductsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ListCategoryView(CartFormView, ListView):
    template_name = 'store/product_cat.html'
    model = Category
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def dispatch(self, request, *args, **kwargs):
        try:
            code = Category.objects.get(code=self.kwargs['code'])
        except:
            raise Http404
        return super().dispatch(request, code)

    def get_context_data(self, **kwargs):
        context = super(ListCategoryView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(code=self.kwargs['code'])
        context['products'] = Product.objects.all()
        return context

    def get_success_url(self):
        return self.request.path


class DetailProductView(CartFormView, DetailView):
    template_name = 'store/product_detail.html'
    model = Product

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        return super().form_valid(form)


class SearchView(CartFormView, ListView):
    context_object_name = 'products'
    template_name = 'store/products.html'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            products = Product.objects.all()
        return products
