from django.shortcuts import render
from .models import Category
from django.views.generic import ListView



class ListCategoryView(ListView):
    template_name = 'index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListCategoryView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
