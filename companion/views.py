from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Companions, Comments
from accounts.models import Users
from .serializers import CompanionSerializer, CommentSerializer
from core.permissons import JWTCookieAuthenticated

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


class CompanionViewSet(viewsets.ModelViewSet):
    queryset = Companions.objects.all()
    serializer_class = CompanionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, JWTCookieAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id != self.request.user.id:
            return Response({'detail': '본인의 글만 수정할 수 있습니다.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id != self.request.user.id:
            return Response({'detail': '본인의 글만 삭제할 수 있습니다.'}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


@ensure_csrf_cookie
def my_view(request):
    response = JsonResponse({'key': 'value'})
    response['Access-Control-Allow-Origin'] = '*'  # 이 부분을 요청하는 도메인에 맞게 수정
    return response


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, JWTCookieAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id != self.request.user.id:
            return Response({'detail': '본인의 댓글만 수정할 수 있습니다.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id != self.request.user.id:
            return Response({'detail': '본인의 댓글만 삭제할 수 있습니다.'}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)