from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - Головна",
        "content": "Буд майданчик Залізниченко"
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - Про нас",
        "content": "Про нас",
        "about_me": "Текст"
    }
    return render(request, "main/about.html", context)
