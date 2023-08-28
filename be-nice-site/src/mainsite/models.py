from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BandMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.ManyToManyField(Instrument)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name: str, genre: str, description: str, location: str):
        genre = Genre.objects.get(name=genre)
        location = Location.objects.get(name=location)
        band = Band.objects.create(name=name, description=description)
        band.genre.set([genre])
        band.location.set([location])
        band.save()
        return band


class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    support = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.location
