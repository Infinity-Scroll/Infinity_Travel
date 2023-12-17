import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from .models import *
from .utils import *

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self, room, user, message):
        message = Message.objects.create(user=user, room=room, message=message)

        return "dd"

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
        print(f"WebSocket DISCONNECT: {close_code}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        room = self.scope["room"]
        user = self.scope["user"]
        message = text_data_json["message"]
        chat_message = await self.save_message(room, user, message)
        print(chat_message)
        # 최근메세지 저장
        update_room_async = database_sync_to_async(
            lambda: setattr(room, "lastest_text", message)
        )
        await update_room_async()
        save_room_async = database_sync_to_async(room.save)
        await save_room_async()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "username": user.nickname,
                "message": chat_message,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        nickname = event["username"]
        # print(event)  # {'type': 'chat.message', "username": user.nickname, 'message': '메세지'}
        await self.send(
            text_data=json.dumps({"username": nickname, "message": message})
        )
