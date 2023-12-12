from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
import datetime


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ["email", "password", "gender", "nickname", "birth"]

    def validate_birth(self, birth):
        today = datetime.date.today()

        if birth > today:
            raise serializers.ValidationError("생년월일이 유효하지 않습니다.")

        return birth

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            gender=validated_data["gender"],
            nickname=validated_data["nickname"],
            birth=validated_data["birth"],
        )
        return user
