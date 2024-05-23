from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(
                    request, f"{username}, Вітаю, Ви успішно авторизовані!"
                )

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("users:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Home - Авторизація",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, f"{user.username}, Вітаю, Ви успішно зареєстровані!"
            )

            if request.POST.get("next", None):
                return HttpResponseRedirect(request.POST.get("next"))

            return HttpResponseRedirect(reverse("main:index"))

    else:
        form = UserRegistrationForm()

    context = {
        "title": "Home - Реєстрація",
        "form": form,
    }
    return render(request, "users/registration.html", context)


@login_required
def profile(request):

    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, " Ваш профіль успішно оновлено!")
            return HttpResponseRedirect(reverse("users:profile"))

    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": "Home - Кабінет",
        "form": form,
    }
    return render(request, "users/profile.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви вийшли з акаунта!")
    auth.logout(request)

    return redirect(reverse("main:index"))
