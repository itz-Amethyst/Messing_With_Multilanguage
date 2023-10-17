from django.http import HttpRequest
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from Product_Module.models import Product


# Create your views here.


def Index(request: HttpRequest):
    context = {
        'data': _('Hello World'),
        'products': Product.objects.all()
    }
    return render(request, 'Home/Index.html', context)