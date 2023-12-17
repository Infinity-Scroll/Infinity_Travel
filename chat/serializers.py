from rest_framework import serializers
from .models import Room, Message
from core.permissions import get_user_id


class RoomSerializer(serializers.ModelSerializer):
    other_user = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ["other_user", "room_name", "lastest_text"]

    def get_other_user(self, room):
        request = self.context.get("request")
        user_id = get_user_id(request)
        other_member = room.member.exclude(id=user_id).first()
        return {
            "nickname": other_member.nickname if other_member else None,
            "chatlink": f"to_{other_member.pk}" if other_member else None,
        }


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["user", "message", "created_at"]
