from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, prod_slug):

    prod = Products.objects.get(slug=prod_slug)

    context = {
        "product": prod,
    }

    return render(request, "goods/product.html", context)
