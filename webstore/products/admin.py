from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Product


class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'language_column', 'description', 'price', 'delivery_until')


admin.site.register(Product, ProductAdmin)
