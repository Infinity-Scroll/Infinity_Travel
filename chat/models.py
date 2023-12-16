from django.db import models
from core.models import TimestampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(TimestampedModel):
    member = models.ManyToManyField(User)
    room_name = models.CharField(max_length=50)
    lastest_text = models.TextField("마지막 대화")


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.nickname}: {self.message}"

    def last_30_messages(self):
        return Message.objects.order_by("-created_at").all()[:30]
