from django.shortcuts import render


def index(request):
    context = {"title": "Home", "content": "Home page - Home"}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")
