from channels.db import database_sync_to_async
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.response import Response
from .models import *

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    return User.objects.get(pk=user_id)


# @database_sync_to_async
# def get_user2_from_roomname(self):
#     roomname = self.scope["url_route"]["kwargs"]["room_name"]
#     _, user2 = roomname.split("_")
#     user2 = get_object_or_404(User, pk=user2)
#     return user2


@database_sync_to_async
def save_message(room, user, message):
    try:
        message = Messages.objects.create(user=user, room=room, message=message)
    except Exception as e:
        print("생성실패", e)
    return {
        "action": "message",
        "user": user.id,
        "roomname": room.room_name,
        "message": message.message,
        # "userprofile": user.image_url.url,
        "username": user.nickname,
        "created_at": str(message.created_at),
    }


async def get_user_from_cookie(self):
    try:
        token = self.scope["cookies"]["access_token"]
        user_id = AccessToken(token)["user_id"]
        user = await get_user(user_id)
        return user

    except TokenError:
        await self.close()
        return Response({"error": "토큰만료"}, status=401)


@database_sync_to_async
def get_room(room_name):
    try:
        room = Rooms.objects.get(room_name=room_name)
        room_members = Room_members.objects.filter(room=room)

        room_members.update(is_visibled=True)
    except Rooms.DoesNotExist:
        return None
    return room
