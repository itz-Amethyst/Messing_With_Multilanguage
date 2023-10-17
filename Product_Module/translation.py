from modeltranslation.translator import TranslationOptions, register
from .models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    # Give fields in Model that you want to be Translate
    fields = ['title']