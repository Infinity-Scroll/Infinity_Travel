import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from .models import *
from django.shortcuts import get_object_or_404
from .utils import *

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = await get_user_from_cookie(self)
        user2 = await get_user2_from_roomname(self)
        room = await get_room(user, user2)
        self.scope["user"] = user
        self.scope["user2"] = user2
        self.scope["room"] = room

        self.room_name = f"{min(user.pk, user2.pk)}_{max(user.pk, user2.pk)}"
        self.room_group_name = f"chat_{self.room_name}"
        print(f"채팅방이름: {self.room_group_name}")
        # 그룹 입장
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        """
        사용자와 WebSocket 연결이 끊겼을 때 호출
        """
        # 누군가 들어오거나 나갈때 마다 db에 채팅내역 저장
        # 채팅방을 삭제하거나 보낸사람 or 받는사람에 대한 추가로직 작성필요
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("유저:", self.scope["user"])
        user = self.scope["user"]
        # 그룹의 이벤트를 받기
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "username": user.nickname,
                "message": message,
            },
        )
        print("receive에서 발생한이벤트")

    async def chat_message(self, event):
        message = event["message"]
        nickname = event["username"]
        print(
            event
        )  # {'type': 'chat.message', "username": user.nickname, 'message': '메세지'}
        await self.send(
            text_data=json.dumps({"username": nickname, "message": message})
        )
        print("chat_message에서 발생한이벤트")

    # def get_redis_messages(self):
    #     for i in self.channel_layer.
