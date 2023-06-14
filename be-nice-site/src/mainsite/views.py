from django.http import request
from django.shortcuts import render
from django.views.generic import (
    ListView,
)


def home(request):
    return render(request, "mainsite/index.html", {"title": "Home"})


def about(request):
    return render(request, "mainsite/about.html", {"title": "About"})
