from channels.db import database_sync_to_async
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.response import Response

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    return User.objects.get(pk=user_id)


@database_sync_to_async
def get_user2_from_roomname(self):
    roomname = self.scope["url_route"]["kwargs"]["room_name"]
    _, user2 = roomname.split("_")
    user2 = get_object_or_404(User, pk=user2)
    return user2


@database_sync_to_async
def save_message(self, message, roomid, userid):
    user = User.objects.get(pk=userid)
    room = Room.objects.get(pk=roomid)
    message = Message.objects.create(user=user, room=room, message=message)

    return {
        "action": "message",
        "user": userid,
        "roomid": roomid,
        "message": message,
        "user": userid,
        # 'userprofile' : user.profileimg.url,  프로필이미지
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
def get_room(user, user2):
    room_name = f"{min(user.pk, user2.pk)}_{max(user.pk, user2.pk)}"
    try:
        room = Room.objects.get(room_name=room_name)
    except Room.DoesNotExist:
        # 해당 room_name의 방이 없으면 새로 생성
        room = Room.objects.create(room_name=room_name).member.add(user, user2)
    return room
