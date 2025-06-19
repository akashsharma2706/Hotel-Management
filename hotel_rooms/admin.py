from django.contrib import admin
from user_auth.models import User
from .models import Hotel,Room, Review, Image, Facilities

admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(Facilities)


class HotelsAdmin(admin.ModelAdmin):   
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "manager":
            kwargs["queryset"] = User.objects.filter(user_type__in=['manager'])
            # print(">>>>>>>>>>", len(kwargs["queryset"]))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

admin.site.register(Hotel, HotelsAdmin)