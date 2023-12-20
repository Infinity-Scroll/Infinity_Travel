from django.contrib import admin
from .models import Place
from .geoCode import get_coordinates

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'category', 'contact', 'website', 'latitude', 'longitude')
    search_fields = ('name', 'address', 'category')

    def save_model(self, request, obj, form, change):
        # 만약 좌표가 비어 있다면
        if not obj.latitude and not obj.longitude and obj.address:
            # 주소를 이용하여 좌표를 가져옴
            coordinates = get_coordinates(obj.address)

            if coordinates:
                obj.latitude, obj.longitude = coordinates

        # 부모의 save_model 메서드 호출
        super().save_model(request, obj, form, change)

admin.site.register(Place, PlaceAdmin)
