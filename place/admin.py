from django.contrib import admin
from .models import Places
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

admin.site.register(Places, PlaceAdmin)
