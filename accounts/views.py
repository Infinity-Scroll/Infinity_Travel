from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import User
from .serializers import UserCreateSerializer, UserSerializer
from .utils import generate_random_nickname
from core.permissions import get_user_id


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # 닉네임이 없는 경우 랜덤 닉네임 생성.
        if "nickname" not in request.data:
            request.data["nickname"] = generate_random_nickname()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = {"message": "이메일 인증을 통해 회원가입을 진행해주세요."}
        return Response(response, status=status.HTTP_200_OK, headers=headers)


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data["message"] = "로그인 성공"

        access_token = response.data["access"]
        refresh_token = response.data["refresh"]

        response.set_cookie("access_token", access_token)
        response.set_cookie("refresh_token", refresh_token)

        return response


class RefreshTokenView(TokenRefreshView):
    # 쿠키에서 엑게스토큰 값을 가져오는것으로 변경
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        access_token = str(serializer.validated_data.get("access"))
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie("access_token", access_token)
        return response


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        user_id = get_user_id(request)
        user = User.objects.get(pk=user_id)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user_id = get_user_id(request)
        user = User.objects.get(pk=user_id)
        serializer = self.serializer_class(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        user = User.objects.get(pk=user_id)
        self.perform_destroy(user)
        return Response(
            {"message": "회원탈퇴가 완료되었습니다. 이용해주셔서 감사합니다."},
            status=status.HTTP_204_NO_CONTENT,
        )


class EmailVerificationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            success_url = "https://www.infinity-travel.shop/front/pages/login.html"
            success_message = "success"
            return redirect(success_url + f"?message={success_message}")
        else:
            return Response(
                {"message": "URL오류입니다."}, status=status.HTTP_400_BAD_REQUEST
            )
