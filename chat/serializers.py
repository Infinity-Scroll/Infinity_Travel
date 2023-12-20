from rest_framework import serializers
from .models import Room, Message
from core.permissions import get_user_id
from django.contrib.auth import get_user_model


User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    other_user = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ["other_user", "room_name", "lastest_text", "updated_at"]

    def get_other_user(self, room):
        request = self.context.get("request")
        user_id = get_user_id(request)
        other_member = room.member.exclude(id=user_id).first()
        return {
            "nickname": other_member.nickname if other_member else None,
            "chatlink": f"to_{other_member.pk}" if other_member else None,
        }


class MessageSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source="user.nickname", read_only=True)
    is_sender = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ["is_sender", "nickname", "message", "created_at"]

    def get_is_sender(self, obj):
        request = self.context.get("request")
        user_id = get_user_id(request)

        return obj.user.pk == user_id
