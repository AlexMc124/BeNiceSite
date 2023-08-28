# Generated by Django 4.2.1 on 2023-08-28 11:59

from django.db import migrations


instruments = [
    {"name": "Guitar"},
    {"name": "Bass"},
    {"name": "Drums"},
    {"name": "Vocals"},
    {"name": "Synth"},
]


def create_instruments(apps, schema_editor):
    Instrument = apps.get_model("mainsite", "Instrument")
    for instrument in instruments:
        Instrument.objects.create(**instrument)


class Migration(migrations.Migration):
    dependencies = [("mainsite", "0002_make_defaults_venue")]

    operations = [
        migrations.RunPython(create_instruments),
    ]