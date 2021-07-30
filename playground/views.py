from django.shortcuts import render
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    queryset = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
