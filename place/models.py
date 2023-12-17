# place/models.py

from django.db import models
from geopy.geocoders import Nominatim
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .geoCode import get_coordinates_from_address

class Place(models.Model):
    name = models.CharField(max_length=255, null=False)  # 이름
    description = models.TextField(null=False)  # 설명
    address = models.CharField(max_length=255, null=False)  # 주소
    category = models.CharField(max_length=255, null=False)  # 분류    
    contact = models.CharField(max_length=20, null=True)  # 찾아오시는 방법
    website = models.URLField()  # 웹사이트
    photo = models.ImageField(upload_to='place_photos/', blank=True, null=False)  # 대표사진
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            # 좌표값이 비어있는 경우, 주소를 이용하여 좌표값을 얻어옴
            coordinates = get_coordinates_from_address(self.address)
            if coordinates:
                self.latitude, self.longitude = coordinates
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'place'
        
class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)  # or use ForeignKey(User, on_delete=models.CASCADE) for user model
    text = models.TextField()
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])  # 0 to 5 rating

    def __str__(self):
        return f"{self.author}'s comment on {self.place.name}"


@receiver(pre_save, sender=Place)
def update_coordinates(sender, instance, **kwargs):
    if not instance.latitude or not instance.longitude:
        # 좌표값이 비어있는 경우, 주소를 이용하여 좌표값을 얻어옴
        coordinates = get_coordinates_from_address(instance.address)
        if coordinates:
            instance.latitude, instance.longitude = coordinates