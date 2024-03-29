# Generated by Django 4.2.1 on 2023-08-28 11:59

from django.db import migrations


bands = [
    {
        "name": "BE N!CE",
        "genre": ["Punk", "Rock"],
        "description": "Four piece punk rock band from London",
        "location": "London",
        "members": [
            {
                "first_name": "Alex",
                "last_name": "McIntosh",
                "instrument": ["Drums"],
            },
            {
                "first_name": "Pol",
                "last_name": "Mills",
                "instrument": ["Vocals"],
            },
            {
                "first_name": "Brett",
                "last_name": "Lee",
                "instrument": ["Guitar"],
            },
            {
                "first_name": "Emily",
                "last_name": "Harris",
                "instrument": ["Bass"],
            },
        ],
    },
    {
        "name": "Ramona Marx",
        "genre": ["Punk", "Rock"],
        "description": "Four Piece Rowdy punk rock band from Hemel",
        "location": "London",
    },
    {
        "name": "French Toast",
        "genre": ["Indie", "Pop"],
        "description": "Arty Singer Songwriting Duo",
        "location": "London",
    },
    {
        "name": "Vagabonds",
        "genre": ["Punk", "Rock"],
        "description": "Four piece punk rock band from London",
        "location": "London",
    },
    {
        "name": "Cherimoya",
        "genre": ["Funk", "Rock", "Psych Rock"],
        "description": "Three piece punk rock band from London",
        "location": "London",
    },
    {
        "name": "Jamch",
        "genre": ["Emo", "Rock"],
        "description": "Energetic Emo Rockers from Hemel",
        "location": "London",
    },
    {
        "name": "Ecto Peach",
        "genre": ["Punk", "Rock"],
        "description": "Energetic Four Piece and nice guys",
        "location": "London",
    },
    {
        "name": "Winnx",
        "genre": ["Punk", "Rock"],
        "description": "Four piece punk rock band from London",
        "location": "London",
    },
    {
        "name": "Admissions",
        "genre": ["Rock"],
        "description": "Five piece classic rock band from London",
        "location": "London",
    },
    {
        "name": "Toxic Rat Party",
        "genre": ["Emo", "Rock"],
        "description": "Four piece punk rock band from Brighton",
        "location": "Brighton",
    },
    {
        "name": "Lost in Space",
        "genre": ["Punk", "Rock"],
        "description": "Veteran Punk Rockers from South London",
        "location": "London",
    },
    {
        "name": "BEAF",
        "genre": ["Punk", "Rock"],
        "description": "BEAFY BOYS rock the house",
        "location": "London",
    },
    {
        "name": "NEW FAITH REACTORS",
        "genre": ["Rock"],
        "description": "Complex riffs from young rockers NFR",
        "location": "London",
    },
    {
        "name": "Vampyr",
        "genre": ["Emo", "Rock", "Punk"],
        "description": "Goth Tinged Vampire fun",
        "location": "London",
    },
    {
        "name": "Divided Compass",
        "genre": ["Rock", "Indie"],
        "description": "Four piece indie rock band from London",
        "location": "London",
    },
    {
        "name": "Stray Foxes",
        "genre": ["Rock", "Pysch Rock"],
        "description": "Young Upstart Three Piece",
        "location": "London",
    },
    {
        "name": "Hypno Gator",
        "genre": ["Rock", "Pysch Rock"],
        "description": "Three Piece Pych Rockers with excellent energy",
        "location": "London",
    },
    {
        "name": "Harry and the Chicks",
        "genre": ["Electronic", "Pop"],
        "description": "Wicked tunes from frontperson Harry supported by the Chicks",
        "location": "London",
    },
]


def create_band(apps, schema_editor):
    Band = apps.get_model("mainsite", "Band")
    BandMember = apps.get_model("mainsite", "BandMember")
    Instrument = apps.get_model("mainsite", "Instrument")
    Genre = apps.get_model("mainsite", "Genre")
    for band in bands:
        genre = Genre.objects.filter(name__in=band["genre"])
        members = []
        if "members" in band:
            for member in band["members"]:
                instruments = Instrument.objects.filter(name__in=member["instrument"])
                members.append(
                    BandMember.objects.create(
                        first_name=member["first_name"],
                        last_name=member["last_name"],
                    )
                )
                members[-1].instrument.set(instruments)
        Band.objects.create(
            name=band["name"],
            description=band["description"],
            location=band["location"],
        )
        Band.objects.last().genre.set(genre)
        Band.objects.last().members.set(members)


class Migration(migrations.Migration):
    dependencies = [("mainsite", "0004_make_defaults_genre")]

    operations = [
        migrations.RunPython(create_band),
    ]
