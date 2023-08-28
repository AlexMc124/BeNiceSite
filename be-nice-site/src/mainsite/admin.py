from django.contrib import admin

from . import models

admin.site.register(models.Band)
admin.site.register(models.BandMember)
admin.site.register(models.Gig)
admin.site.register(models.Instrument)
admin.site.register(models.Genre)
