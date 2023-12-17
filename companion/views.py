from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Companion, Comment, Tag
from .serializers import CompanionSerializer, CommentSerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


class CompanionViewSet(viewsets.ModelViewSet):
    queryset = Companion.objects.all()
    serializer_class = CompanionSerializer

    # JWTAuthentication 적용
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # JWTAuthentication 적용하지 않는 액션들에 대한 decorator
    @action(detail=False, methods=['get'])
    def list_without_auth(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def retrieve_without_auth(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@ensure_csrf_cookie
def my_view(request):
    response = JsonResponse({'key': 'value'})
    response['Access-Control-Allow-Origin'] = '*'  # 이 부분을 요청하는 도메인에 맞게 수정
    return response


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer