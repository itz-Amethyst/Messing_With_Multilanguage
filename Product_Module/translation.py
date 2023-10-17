from modeltranslation.translator import TranslationOptions, register
from .models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    # Give fields in Model that you want to be Translate

    #! Note: when you create a product in admin for e.g.m you have title , title[fa], title[en] it will fill title fa either because of site language depends in setting
    fields = ['title', 'description']