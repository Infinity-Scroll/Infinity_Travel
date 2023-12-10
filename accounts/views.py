from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import generics, status, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import User, Profile
from .serializers import UserCreateSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        profile = Profile.objects.create(user=user)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


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
