from django.urls import path
from .views import (
    RoomListAPIView,
    MessageListAPIView,
    RoominvisibleAPIView,
    RoomCreateAPIView,
)


urlpatterns = [
    path("roomlist/", RoomListAPIView.as_view(), name="roomlist"),
    path("roomcreate/", RoomCreateAPIView.as_view(), name="room_create"),
    path("<str:room_name>/", MessageListAPIView.as_view(), name="room_message"),
    path(
        "roominvisible/<str:room_name>/",
        RoominvisibleAPIView.as_view(),
        name="room_invisible",
    ),
]
