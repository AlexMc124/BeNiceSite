# Generated by Django 4.2.1 on 2023-08-28 11:59

from django.db import migrations
from datetime import date, time

gigs = [
    {
        "date": date(2022, 12, 9),
        "time": time(19, 00),
        "venue": "The Earl Ferrers",
        "price": 0.00,
        "support": ["Lost in Space"],
        "description": "Free Gig, the BE N!CE debut!",
    },
    {
        "date": date(2023, 1, 21),
        "time": time(17, 00),
        "venue": "The Amersham Arms",
        "price": 5.00,
        "support": None,
        "description": """BE N!CE play the Amersham Arms, with promoter
        underground sound and lots of other bands""",
    },
    {
        "date": date(2023, 2, 7),
        "time": time(20, 00),
        "venue": "New Cross Inn",
        "price": 8.00,
        "support": None,
        "description": """BE N!CE have their first headline show at the New Cross Inn!""",
    },
    {
        "date": date(2023, 3, 17),
        "time": time(18, 30),
        "venue": "The Beehive",
        "price": 8.00,
        "support": None,
        "description": """BE N!CE visit Bow for the first time, play some wicked tunes!""",
    },
    {
        "date": date(2023, 3, 30),
        "time": time(19, 00),
        "venue": "The Horn",
        "price": 8.00,
        "support": ["Admissions"],
        "description": """BE N!CE head out of town to play with Admissions in Hemel Hempstead!""",
    },
    {
        "date": date(2023, 4, 9),
        "time": time(19, 00),
        "venue": "The Star in Shoreditch",
        "price": 8.00,
        "support": ["BEAF", "Vagabonds"],
        "description": """BE N!CE venture into London to play with 
        friends BEAF and Vagabonds for young meat fest!""",
    },
    {
        "date": date(2023, 4, 16),
        "time": time(17, 00),
        "venue": "The Good Mixer",
        "price": 0.00,
        "support": ["Divided Compass"],
        "description": """BE N!CE enter Camden for the first time for a free show!""",
    },
    {
        "date": date(2023, 4, 29),
        "time": time(19, 00),
        "venue": "Friars Inn",
        "price": 10.00,
        "support": ["BEAF", "Vagabonds", "Ramona Marx"],
        "description": """BE N!CE reunite with young meat fest to support Ramona Marx!""",
    },
    {
        "date": date(2023, 5, 12),
        "time": time(17, 00),
        "venue": "The Macbeth",
        "price": 10.00,
        "support": None,
        "description": """BE N!CE play the Macbeth for the first time with promotor Half Numb!""",
    },
    {
        "date": date(2023, 5, 30),
        "time": time(17, 00),
        "venue": "The Good Mixer",
        "price": 00.00,
        "support": ["NEW FAITH REACTORS", "Vampyr"],
        "description": """BE N!CE return to the Good Mixer!""",
    },
    {
        "date": date(2023, 5, 31),
        "time": time(19, 30),
        "venue": "The Horn",
        "price": 8.00,
        "support": None,
        "description": """BE N!CE return to The Horn!""",
    },
    {
        "date": date(2023, 6, 15),
        "time": time(19, 30),
        "venue": "The Old Town Hall",
        "price": 8.00,
        "support": ["Ramona Marx", "Stray Foxes"],
        "description": """BE N!CE Head to Hemel to support Ramona Marx!""",
    },
    {
        "date": date(2023, 6, 29),
        "time": time(15, 30),
        "venue": "The Amersham Arms",
        "price": 8.00,
        "support": ["Hypno Gator", "Harry and the Chicks"],
        "description": """BE N!CE return to the Amersham Arms with Half Numb for a wicked showcase!""",
    },
    {
        "date": date(2023, 7, 22),
        "time": time(19, 00),
        "venue": "Poco Loco",
        "price": 10.00,
        "support": ["Toxic Rat Party"],
        "description": """BE N!CE venture to Chatham to play iconic queer
        venue Poco Loco with support from emo rockers Toxic Rat Party!""",
    },
    {
        "date": date(2023, 7, 28),
        "time": time(18, 00),
        "venue": "The Fighting Cocks",
        "price": 10.00,
        "support": None,
        "description": """BE N!CE play Kingston for the first time at the 
        iconic Fighting Cocks!""",
    },
    {
        "date": date(2023, 7, 29),
        "time": time(18, 00),
        "venue": "The Macbeth",
        "price": 10.00,
        "support": ["French Toast"],
        "description": """Back with Half Numb at the Macbeth!""",
    },
    {
        "date": date(2023, 8, 3),
        "time": time(18, 00),
        "venue": "The Horns",
        "price": 10.00,
        "support": ["Jamch", "Cherimoya"],
        "description": """BE N!CE head to Watford to play
        for JAMCHs release party!""",
    },
    {
        "date": date(2023, 8, 11),
        "time": time(18, 00),
        "venue": "The Engine Rooms",
        "price": 10.00,
        "support": ["Winnx", "Ecto Peach"],
        "description": """BE N!CE play cool queer space Engine
        Rooms with Ecto Peach supporting Winnx!""",
    },
]


def create_band(apps, schema_editor):
    Gig = apps.get_model("mainsite", "Gig")
    Band = apps.get_model("mainsite", "Band")
    Venue = apps.get_model("mainsite", "Venue")
    for gig in gigs:
        gig["venue"] = Venue.objects.get(name=gig["venue"])
        gig["date"] = gig["date"].strftime("%Y-%m-%d")
        gig["time"] = gig["time"].strftime("%H:%M")
        gig["description"] = gig["description"].replace("\n", "")
        if gig["support"]:
            gig["support"] = [Band.objects.get(name=band) for band in gig["support"]]
        else:
            # remove the key if it's empty
            del gig["support"]
        Gig.objects.create(**gig)


class Migration(migrations.Migration):
    dependencies = [("mainsite", "0005_make_defaults_bands")]

    operations = [
        migrations.RunPython(create_band),
    ]