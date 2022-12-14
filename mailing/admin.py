from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Mailing


@admin.register(Mailing)
class MailingAdmin(ModelAdmin):
    pass
