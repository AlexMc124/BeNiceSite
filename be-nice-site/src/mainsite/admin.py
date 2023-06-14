from django.contrib import admin

from .models import Band, BandMember, Gig

admin.site.register(Band)
admin.site.register(BandMember)
admin.site.register(Gig)
