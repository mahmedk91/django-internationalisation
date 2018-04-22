from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=60, null=False, blank=False)
    description = models.TextField('Description', null=True, blank=True)
    price = models.DecimalField('Price', max_digits=5, decimal_places=2, null=False, blank=False)
    delivery_until = models.DateField('Delivery until', null=False, blank=False)
    image = models.ImageField('Product Image', null=True, blank=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name