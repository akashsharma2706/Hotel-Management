from django.contrib import admin
from .models import Hotel,Room, Review, Location, Facilities, Hotelimage, Roomimage

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Location)
admin.site.register(Facilities)
admin.site.register(Hotelimage)
admin.site.register(Roomimage)

