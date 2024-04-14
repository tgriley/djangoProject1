from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, "home.html", {'environment': settings.ENVIRONMENT})
