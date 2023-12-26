from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from dotenv import load_dotenv
import os
import datetime

load_dotenv()


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
            is_active=False,
        )
        token = default_token_generator.make_token(user)

        verification_link = f"https://{os.environ.get('HOST')}/accounts/verify-email/{urlsafe_base64_encode(force_bytes(user.pk))}/{token}/"
        message = f"가입을 완료하려면 다음 링크를 클릭하세요: {verification_link}"
        email_message = EmailMessage(
            subject="Infinify_Travel 회원가입 인증 메일입니다.",
            body=message,
            to=[validated_data["email"]],
        )
        email_message.send()
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["email", "nickname", "image_url", "introduction", "gender", "birth"]

    def validate_birth(self, birth):
        today = datetime.date.today()

        if birth > today:
            raise serializers.ValidationError("생년월일이 유효하지 않습니다.")

        return birth
