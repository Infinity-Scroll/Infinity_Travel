from django.test import TestCase, Client
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async

User = get_user_model()
room_name = "1_2"
email = "test12@test12.com"
password = "testpw123"
loginurl = "/accounts/login/"
testmessage = "hello world"


class MyTests(TestCase):
    def setUp(self):
        print("----------유저 생성-----------")
        self.user = User.objects.create_user(
            email=email,
            password=password,
            gender="Male",
            nickname="test",
            birth="2023-11-11",
        )
        self.user2 = User.objects.create_user(
            email="test222@test22.com",
            password="testpassword2222",
            gender="Male",
            nickname="test",
            birth="2023-11-11",
        )
        client = Client()
        login = client.login(email=email, password=password)
        self.assertTrue(login)

    @database_sync_to_async
    def login_user(self, client):
        response = client.post(loginurl, {"email": email, "password": password})
        return client

    async def test_my_consumer(self):
        communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "")
        communicator.scope["url_route"] = {
            "args": (),
            "kwargs": {"room_name": room_name},
        }
        client = await self.login_user(Client())
        self.assertTrue(client.login)

        cookies = client.cookies.output(header="", sep=";").strip().split("; ")
        communicator.scope["cookies"] = {}
        for cookie in cookies:
            key, value = cookie.split("=")
            communicator.scope["cookies"][key] = value

        connected, subprotocol_ = await communicator.connect()
        self.assertTrue(connected)

        print("----------메세지 전송 테스트-----------")
        await communicator.send_json_to({"message": testmessage})
        response = await communicator.receive_json_from()
        print("받은 메세지:", response)
        assert response["message"]["message"] == testmessage

        await communicator.disconnect()
