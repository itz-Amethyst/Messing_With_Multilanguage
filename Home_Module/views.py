from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def Index(request: HttpRequest):
    return render(request, 'Home/Index.html', {})