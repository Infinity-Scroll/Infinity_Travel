from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ["email", "password", "gender", "nickname", "birth"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            gender=validated_data["gender"],
            nickname=validated_data["nickname"],
            birth=validated_data["birth"],
        )
        return user