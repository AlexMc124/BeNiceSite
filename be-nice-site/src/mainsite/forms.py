from django import forms as django_forms

from mainsite import models


def get_location_choices() -> list[models.Location]:
    return [
        (location.name, location.name) for location in models.Location.objects.all()
    ]


def get_genre_choices() -> list[models.Genre]:
    return [(genre.name, genre.name) for genre in models.Genre.objects.all()]


class AddBandForm(django_forms.Form):
    name = django_forms.CharField(label="Name", max_length=100)
    genre = django_forms.ChoiceField(label="Genre", choices=get_genre_choices())
    location = django_forms.ChoiceField(
        label="Location", choices=get_location_choices()
    )
    description = django_forms.CharField(label="Description", max_length=100)


def get_band_choices() -> list[models.Band]:
    return [(band.id, band.name) for band in models.Band.objects.all()]


def get_instrument_choices() -> list[models.Instrument]:
    return [(band.id, band.name) for band in models.Instrument.objects.all()]


class AddBandMemberForm(django_forms.Form):
    first_name = django_forms.CharField(label="First Name", max_length=100)
    last_name = django_forms.CharField(label="Last Name", max_length=100)
    instrument = django_forms.ChoiceField(choices=get_instrument_choices())
    band = django_forms.ChoiceField(choices=get_band_choices())
