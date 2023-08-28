from datetime import timezone
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from mainsite import forms as mainsite_forms
from mainsite import models


def home(request):
    return render(request, "mainsite/index.html", {"title": "Home"})


def about(request):
    return render(request, "mainsite/about.html", {"title": "About"})


class AddBandMember(generic.FormView):
    form_class = mainsite_forms.AddBandMemberForm
    template_name = "mainsite/forms/add_band_member.html"

    def form_valid(self, form):
        band = models.Band(
            name=form.cleaned_data["name"],
            genre=form.cleaned_data["genre"],
            description=form.cleaned_data["description"],
            membership=form.cleaned_data["membership"],
        )
        band.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("mainsite-gigs")


class AddBand(generic.FormView):
    form_class = mainsite_forms.AddBandForm
    template_name = "mainsite/forms/add_band_form.html"

    def form_valid(self, form):
        models.Band.create(
            name=form.cleaned_data["name"],
            genre=form.cleaned_data["genre"],
            description=form.cleaned_data["description"],
            location=form.cleaned_data["location"],
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("mainsite-band")


class BandDetailView(generic.DetailView):
    model = models.Band

    def get(self, request, *args, **kwargs):
        band = models.Band.objects.get(name=kwargs["name"])
        return render(
            request,
            "mainsite/bands/band_detail.html",
            {"band": band, "title": band.name},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Band"
        return context


class BandListView(generic.ListView):
    model = models.Band
    template_name = "mainsite/bands/bands.html"
    context_object_name = "bands"
    ordering = ["date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Bands"
        return context

    def get_queryset(self):
        return models.Band.objects.order_by("name")


class GigListView(generic.ListView):
    model = models.Gig
    template_name = "mainsite/gigs.html"
    context_object_name = "gigs"
    ordering = ["date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Gigs"
        return context

    def get_queryset(self):
        return models.Gig.objects.order_by("date")
