from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Головна",
        "content": "Буд майданчик Залізниченко",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "Home - Про нас", "content": "Про нас", "about_me": "Текст"}
    return render(request, "main/about.html", context)
