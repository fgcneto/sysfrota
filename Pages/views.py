from django.views.generic import TemplateView
from django.shortcuts import render


def home(request):
    if request.user.is_superuser:
        return home_admin(request)
    else:
        return home_user(request)


def home_user(request):
    return render(request, "Usuario/home_user.html")


def home_admin(request):
    return render(request, "Usuario/home_admin.html")
