from django.contrib import admin
from .models import Musician, Album, Group, Track, Organizer, Contract, MusicianContractStatus

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Group)
admin.site.register(Track)
admin.site.register(Organizer)
admin.site.register(Contract)
admin.site.register(MusicianContractStatus)