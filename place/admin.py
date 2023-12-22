from django.contrib import admin
from .models import Places,Place_comments
from .geoCode import get_coordinates

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'category', 'contact', 'website', 'latitude', 'longitude')
    search_fields = ('name', 'address', 'category')

    def save_model(self, request, obj, form, change):
        if not obj.latitude and not obj.longitude and obj.address:
            coordinates = get_coordinates(obj.address)

            if coordinates:
                obj.latitude, obj.longitude = coordinates

        super().save_model(request, obj, form, change)

@admin.register(Place_comments)
class PlaceCommentsAdmin(admin.ModelAdmin):
    list_display = ('place', 'user', 'content', 'rating')
    list_filter = ('place', 'user', 'rating')
    search_fields = ('place__name', 'user__username', 'content')

admin.site.register(Places, PlaceAdmin)
