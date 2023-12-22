from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Places, Place_comments
from .serializers import PlaceSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from core.permissions import JWTCookieIsOwnerorReadOnly, IsOwnerOrReadOnly

class JWTCookieIsOwnerOrReadOnlyMixin:
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [JWTCookieIsOwnerorReadOnly()]
        return [AllowAny()]
    
    
class PlaceViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    
class CommentViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Place_comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Comment를 생성할 때, 현재 요청을 보낸 사용자를 Comment의 user에 설정
        serializer.save(user=self.request.user)