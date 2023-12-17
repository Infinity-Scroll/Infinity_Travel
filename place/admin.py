# place/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Place
from .geoCode import get_coordinates_from_address

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'category', 'display_photo')

    def display_photo(self, obj):
        return obj.photo.url if obj.photo else 'No Image'

    display_photo.short_description = 'Photo'

    def save_model(self, request, obj, form, change):
        # 주소가 입력되어 있고, 좌표값이 비어 있는 경우에만 자동으로 좌표값 생성
        print ( " 제대로 작동하고 있는 지 테스트 ")
        if obj.address and (not obj.latitude or not obj.longitude):
            print ( " 제대로 작동하고 있는 지 테스트  2222222")
            coordinates = get_coordinates_from_address(obj.address)
            if coordinates:
                obj.latitude, obj.longitude = coordinates
        super().save_model(request, obj, form, change)

