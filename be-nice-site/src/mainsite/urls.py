from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="mainsite-home"),
    path("about/", views.about, name="mainsite-about"),
    path("gigs/", views.GigListView.as_view(), name="mainsite-gigs"),
    path("bands/", views.BandListView.as_view(), name="mainsite-bands"),
    path("band/<str:name>/", views.BandDetailView.as_view(), name="mainsite-band"),
    path(
        "add_band_member/",
        views.AddBandMember.as_view(),
        name="mainsite-add-band-member",
    ),
    path(
        "add_band/",
        views.AddBand.as_view(),
        name="mainsite-add-band",
    ),
]
