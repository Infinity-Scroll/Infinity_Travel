# models.py

from django.db import models
from place.models import Place
from django.conf import settings

class Planner(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    public = models.BooleanField(default=True) # 공개 여부 플래그 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 작성자 

    def __str__(self):
        return self.title

class PeriodEvent(models.Model):
    planner = models.ForeignKey(Planner, related_name='period_events', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    

    def __str__(self):
        return self.title

class DateEvent(models.Model):
    period_event = models.ForeignKey(PeriodEvent, related_name='date_events', on_delete=models.CASCADE)
    event_date = models.DateField()
    places = models.ManyToManyField(Place, related_name='date_events', blank=True)

    def __str__(self):
        return f"{self.period_event.title} - {self.event_date}"


class DateEventPlace(models.Model):
    order = models.IntegerField()
    date_event = models.ForeignKey(DateEvent, related_name='date_event_places', on_delete=models.CASCADE)
    place = models.ForeignKey(Place, related_name='date_event_places', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.date_event} - {self.place}"