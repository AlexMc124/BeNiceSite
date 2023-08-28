from django import forms as django_forms

from mainsite import models


class AddBandForm(django_forms.ModelForm):
    class Meta:
        model = models.Band
        fields = ["name", "genre", "description", "location"]


class AddBandMemberForm(django_forms.ModelForm):
    class Meta:
        model = models.BandMember
        fields = ["first_name", "last_name", "instrument"]


class DateInput(django_forms.DateInput):
    input_type = "date"


class TimeInput(django_forms.TimeInput):
    input_type = "time"


class AddGigForm(django_forms.ModelForm):
    class Meta:
        model = models.Gig
        fields = ["date", "time", "venue", "price", "support", "description"]
        widgets = {
            "date": DateInput(),
            "time": TimeInput(),
        }
