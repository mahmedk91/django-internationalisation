from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    price = models.DecimalField(_('model.product.price'), max_digits=5, decimal_places=2, null=False, blank=False)
    delivery_until = models.DateField(_('model.product.delivery_until'), null=False, blank=False)
    image = models.ImageField(_('model.product.image'), null=True, blank=True)

    translations = TranslatedFields(
        name=models.CharField(_('model.product.name'), max_length=60, null=False, blank=False),
        description=models.TextField(_('model.product.description'), null=True, blank=True)
    )

    class Meta:
        db_table = 'products'
        verbose_name = _('model.product')
        verbose_name_plural = _('model.product.s')

    def __str__(self):
        return self.name
