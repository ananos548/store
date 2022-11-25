import logging

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormMixin, BaseFormView

from cart.forms import CartForm
from .models import Category, Product
from django.views.generic import ListView, DetailView

logger = logging.getLogger(__name__)


class MainView(ListView):
    template_name = 'store/index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ListCategoryView(ListView, BaseFormView):
    template_name = 'store/product_cat.html'
    model = Category
    slug_field = 'code'
    slug_url_kwarg = 'code'
    form_class = CartForm

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


class DetailProductView(DetailView, BaseFormView):
    template_name = 'store/product_detail.html'
    model = Product
    form_class = CartForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        return super().form_valid(form)
