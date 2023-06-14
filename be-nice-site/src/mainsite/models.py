from django.db import models


class BandMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    membership = models.ManyToManyField(BandMember)

    def __str__(self):
        return self.name


class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    support = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.location
