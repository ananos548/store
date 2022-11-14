from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass
