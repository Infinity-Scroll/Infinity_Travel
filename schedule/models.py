# models.py

from django.db import models
from place.models import Place

class Planner(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

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
    description = models.TextField()
    place = models.ForeignKey(Place, related_name='date_events', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.period_event.title} - {self.event_date}"
