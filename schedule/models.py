from django.db import models
from place.models import Places
from core.models import AreaModel
from place.geoCode import get_coordinates
from accounts.models import User
from datetime import timedelta

class Planners(AreaModel, models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    public_flag = models.BooleanField(default=True)  # 공개 여부 플래그
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_period_events()

    def create_period_events(self):
        PeriodEvents.objects.create(
            planner=self,
            start_date=self.start_date,
            end_date=self.end_date,
            area=self.area 
        )


class PeriodEvents(AreaModel, models.Model):
    planner = models.ForeignKey(Planners, related_name='period_events', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    latitude = models.FloatField(blank=True, null=True, editable=False)
    longitude = models.FloatField(blank=True, null=True, editable=False)

    def __str__(self):
        return f"{self.planner.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.latitude and not self.longitude and self.area:
            coordinates = get_coordinates(self.area)
            if coordinates:
                self.latitude, self.longitude = coordinates
        super(PeriodEvents, self).save(*args, **kwargs)
        self.create_date_events()

    def create_date_events(self):
        # DateEvents 생성
        date_range = [self.start_date + timedelta(days=x) for x in range((self.end_date - self.start_date).days + 1)]

        for event_date in date_range:
            date_event, created = DateEvents.objects.get_or_create(
                period_event=self,
                event_date=event_date                
            )


class DateEvents(models.Model):
    period_event = models.ForeignKey(PeriodEvents, related_name='date_events', on_delete=models.CASCADE)
    event_date = models.DateField()
    place = models.ManyToManyField(Places, related_name='date_events', blank=True)

    def __str__(self):
        return f"{self.period_event.pk} - {self.event_date}"

    def save(self, *args, **kwargs):
        super(DateEvents, self).save(*args, **kwargs)


class DateEventPlaces(models.Model):
    date_event = models.ForeignKey(DateEvents, related_name='date_event_places', on_delete=models.CASCADE)
    order = models.IntegerField()
    place = models.ForeignKey(Places, related_name='date_event_places', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} - {self.date_event} - {self.place}"
    
    @classmethod
    def add_places_to_date_event(cls, date_event, place_ids):
        # date_event에 연결된 DateEventPlaces 가져오기
        date_event_places = cls.objects.filter(date_event=date_event)

        # 기존의 DateEventPlaces 삭제
        date_event_places.delete()

        # 새로운 DateEventPlaces 생성
        for order, place_id in enumerate(place_ids, start=1):
            place = Places.objects.get(pk=place_id)
            cls.objects.create(date_event=date_event, order=order, place=place)