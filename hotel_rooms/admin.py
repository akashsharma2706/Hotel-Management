from django.contrib import admin
from .models import Hotel,Room, Review, Image, Facilities


class hotelAdmin(admin.ModelAdmin):
  list_display = ("name",)
  list_filter = ['name']


class RoomAdmin(admin.ModelAdmin):
  list_display = ("room_number",)
  list_filter = ['room_type']


class ReviewAdmin(admin.ModelAdmin):
   list_display = ("comment",)
   list_filter = ['star_rating']


admin.site.register(Hotel, hotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Image)
admin.site.register(Facilities)






