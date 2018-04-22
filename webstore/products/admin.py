from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'delivery_until')


admin.site.register(Product, ProductAdmin)
