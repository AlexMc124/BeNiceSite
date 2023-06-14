from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="mainsite-home"),
    path("about/", views.about, name="mainsite-about"),
]
