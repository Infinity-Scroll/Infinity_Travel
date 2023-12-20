from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
from .geoCode import get_coordinates
from django.conf import settings

class Place(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    address = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=20, null=True, blank=True)  # 선택 사항으로 변경
    website = models.URLField(null=True, blank=True)  # 선택 사항으로 변경
    photo = models.ImageField(upload_to='place_photos/', blank=False, null=False)  # 필수 입력으로 변경
    latitude = models.FloatField(blank=True, null=True,editable=False)
    longitude = models.FloatField(blank=True, null=True,editable=False)
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

    def save(self, *args, **kwargs):
        # 만약 주소가 비어 있다면
        if not self.latitude and not self.longitude and self.address:
            # 주소를 이용하여 좌표를 가져옴
            coordinates = get_coordinates(self.address)
            
            if coordinates:
                self.latitude, self.longitude = coordinates

        # 부모의 save 메서드 호출
        super(Place, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'place'
        
class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])  # 0 to 5 rating

    def __str__(self):
        return f"{self.author}'s commen t on {self.place.name}"
