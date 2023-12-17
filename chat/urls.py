from django.urls import path
from .views import RoomListAPIView, MessageListAPIView


urlpatterns = [
    path("roomlist/", RoomListAPIView.as_view(), name="roomlist"),
    path("<str:room_name>/", MessageListAPIView.as_view(), name="room_message"),
]
