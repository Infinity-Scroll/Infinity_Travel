from django.db import models
from core.models import TimestampedModel

class Companion(TimestampedModel):
    STATUS_CHOICES = (
        ('A', '모집중'),
        ('Z', '모집완료'),
    )

    title = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    view_count = models.IntegerField(default=0, null=False)
    region = models.CharField(max_length=20, null=True)
    image = models.ImageField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A', blank=True)

    def __str__(self):
        return self.title