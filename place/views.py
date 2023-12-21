from rest_framework import viewsets
from .models import Places, Comments
from .serializers import PlaceSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.shortcuts import render, redirect

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny] # 상시 확인 가능 
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny] # 상시 확인 가능 