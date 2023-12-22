from rest_framework import viewsets
from .models import Places, Place_comments
from .serializers import PlaceSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from core.permissions import *

class JWTCookieIsOwnerOrReadOnlyMixin:
    def get_permissions(self):
        if getattr(self, 'action', None) in ['create', 'update', 'partial_update', 'destroy']:
            return [JWTCookieIsOwnerorReadOnly()]
        return [AllowAny()]
class PlaceViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    
class CommentViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Place_comments.objects.all()
    serializer_class = CommentSerializer