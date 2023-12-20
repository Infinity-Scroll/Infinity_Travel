from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from core.permissions import get_user_id
from django.shortcuts import get_object_or_404
from .models import Room
from .serializers import *


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        user_id = get_user_id(self.request)

        return (
            Room.objects.filter(member=user_id)
            .exclude(invisible=user_id)
            .order_by("-updated_at")
        )


class RoominvisibleAPIView(APIView):
    def get(self, request, room_name):
        user_id = get_user_id(request)
        try:
            room = Room.objects.get(room_name=room_name)
            room.invisible.add(user_id)
            room.save()
            return Response(
                {"message": "채팅방을 삭제했습니다."},
                status=status.HTTP_200_OK,
            )
        except Room.DoesNotExist:
            return Response(
                {"error": "해당하는 채팅방을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )


class MessageListPagination(PageNumberPagination):
    page_size = 30
    # 개수를 지정하여 불러올 때
    page_size_query_param = "page_size"
    max_page_size = 200


class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = MessageListPagination

    def get_queryset(self):
        user_id = get_user_id(self.request)
        room_name = self.kwargs.get("room_name", "")
        room = get_object_or_404(Room, room_name=room_name, member=user_id)
        queryset = Message.objects.filter(room=room).order_by("-created_at")
        return queryset


## 채팅에서 메세지 생성 시 유저 사라지는 문제
