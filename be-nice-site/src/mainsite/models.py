from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)

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
    location = models.CharField(max_length=100)
    members = models.ManyToManyField(BandMember, blank=True)

    def __str__(self):
        return self.name


class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    support = models.ManyToManyField(Band, blank=True, related_name="support")
    description = models.TextField()

    def __str__(self):
        return self.location
