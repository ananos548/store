import logging

from django.http import Http404

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


class ListCategoryView(ListView):
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


class DetailProductView(DetailView):
    template_name = 'store/product_detail.html'
    model = Product
