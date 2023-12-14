import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Scope:", self.scope)
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        token = self.scope["cookies"]["access_token"]
        print("쿠키_access_token:", token)
        user_id = AccessToken(token)
        print("user_id:", user_id["user_id"])
        # 그룹 입장
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # 권한 체크 필요
        await self.accept()

    async def disconnect(self, close_code):
        # 떠나기
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # print("Message:", message)

        # 그룹의 이벤트를 받기
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]
        print(event)  # {'type': 'chat.message', 'message': 'ㄴㅇ'}
        await self.send(text_data=json.dumps({"message": message}))
