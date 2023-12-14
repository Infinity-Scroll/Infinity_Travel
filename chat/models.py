from django.db import models
from core.models import TimestampedModel
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Room(TimestampedModel):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="room_sender"
    )
    sender_unread_count = models.IntegerField()
    sender_is_deleted = models.BooleanField()

    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="room_receiver"
    )
    receiver_unread_count = models.IntegerField()
    receiver_is_deleted = models.BooleanField()

    lastest_text = models.TextField("마지막 대화")


class Message(TimestampedModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text_message = models.TextField()
    is_read = models.BooleanField()
