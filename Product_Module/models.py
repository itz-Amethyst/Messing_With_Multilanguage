from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length = 300, verbose_name = _('Title'))
    description = models.TextField(max_length = 300, blank = True, verbose_name = _('Description'))
    price = models.IntegerField(default = 0, verbose_name = _('Price'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.title} / {self.price}'