from django.db import models
from core.models import TimestampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(TimestampedModel):
    member = models.ManyToManyField(User, related_name="member")
    room_name = models.CharField(max_length=50)
    invisible = models.ManyToManyField(User, "room_invisible")
    lastest_text = models.TextField("마지막 대화")


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.nickname}: {self.message}"
