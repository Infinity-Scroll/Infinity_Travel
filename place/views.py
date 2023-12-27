from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
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
    
    def get_queryset(self):
        queryset = Places.objects.all()
        name_query = self.request.query_params.get('name', None)

        if name_query:
            queryset = queryset.filter(Q(name__icontains=name_query) | Q(description__icontains=name_query))

        return queryset
    
class CommentViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Place_comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Comment를 생성할 때, 현재 요청을 보낸 사용자를 Comment의 user에 설정
        serializer.save(user=self.request.user)
        
# 장소 검색을 위한 함수
def search_places(request):
    search_term = request.GET.get('search_term', '')
    
    # 검색어로 name 또는 address 필드를 검색
    places = Places.objects.filter(Q(name__icontains=search_term) | Q(address__icontains=search_term))
    
    # 검색 결과를 JSON 형태로 반환
    data = {
        'places': [{'name': place.name, 'address': place.address} for place in places]
    }
    
    return JsonResponse(data)