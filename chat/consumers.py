import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async


User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_user(self, user_id):
        return User.objects.get(pk=user_id)

    async def connect(self):
        print("Scope:", self.scope)
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        try:
            token = self.scope["cookies"]["access_token"]
            user_id = AccessToken(token)["user_id"]

            user = await self.get_user(user_id)
            self.scope["user"] = user
            print(user)
            # print("user", self.scope["user"]) #AnonymousUser

        except TokenError:
            await self.close()
            return Response({"error": "토큰만료"}, status=401)

        # 그룹 입장
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        """
        사용자와 WebSocket 연결이 끊겼을 때 호출
        """
        # 채팅방을 삭제하거나 보낸사람 or 받는사람에 대한 추가로직 작성필요
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        user = self.scope["user"]
        # 그룹의 이벤트를 받기
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat.message", "username": user.nickname, "message": message},
        )

    async def chat_message(self, event):
        message = event["message"]
        user = self.scope["user"]
        print(event)  # {'type': 'chat.message', "username": user.pk, 'message': 'ㄴㅇ'}
        await self.send(
            text_data=json.dumps({"username": user.nickname, "message": message})
        )
