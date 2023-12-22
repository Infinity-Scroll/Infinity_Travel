from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from core.permissions import IsOwner, JWTCookieAuthenticated, JWTCookieIsOwnerorReadOnly
from .models import Planners, PeriodEvents, DateEvents, DateEventPlaces
from .serializers import (
    PlannerSerializer, PeriodEventSerializer, DateEventSerializer,
    DateEventPlaceSerializer
)

# CUD의 경우는 작성자만 가능하도록 변경
class JWTCookieIsOwnerOrReadOnlyMixin:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [JWTCookieIsOwnerorReadOnly()]
        return [AllowAny()]

# 최상위 Planner에 대한 CRUD 뷰
class PlannerViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer
    

# PeriodEvent에 대한 CRUD 뷰
class PeriodEventViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = PeriodEvents.objects.all()
    serializer_class = PeriodEventSerializer

# DateEvent에 대한 CRUD 뷰
class DateEventViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = DateEvents.objects.all()
    serializer_class = DateEventSerializer

# DateEventPlace에 대한 CRUD 뷰
class DateEventPlaceViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = DateEventPlaces.objects.all()
    serializer_class = DateEventPlaceSerializer

# 나머지 일반적인 기능을 수행하는 view들
class PlannerListCreateAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer

class PlannerDetailAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer

