from rest_framework import generics
from core.permissions import get_user_id
from django.shortcuts import get_object_or_404
from .models import Room
from .serializers import *


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        user_id = get_user_id(self.request)

        return Room.objects.filter(member=user_id)


class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = get_user_id(self.request)
        room_name = self.kwargs.get("room_name", "")
        room = get_object_or_404(Room, room_name=room_name, member=user_id)
        queryset = Message.objects.filter(room=room).order_by("-created_at")[:30]
        return queryset
