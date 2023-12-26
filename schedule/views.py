from django.urls import reverse
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.permissions import IsOwner, JWTCookieAuthenticated, JWTCookieIsOwnerorReadOnly
from .models import Planners, PeriodEvents, DateEvents, DateEventPlaces
from .serializers import (
    PlannerSerializer, PeriodEventSerializer, DateEventSerializer,
    DateEventPlaceSerializer
)

class JWTCookieIsOwnerOrReadOnlyMixin:
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [JWTCookieIsOwnerorReadOnly()]
        return [AllowAny()]

class PlannerViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer
    
    def get_queryset(self):
        queryset = Planners.objects.all()
        name_query = self.request.query_params.get('name', None)
        if name_query is not None:
            queryset = queryset.filter(name__icontains=name_query)
        return queryset


class PeriodEventViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = PeriodEvents.objects.all()
    serializer_class = PeriodEventSerializer


class DateEventViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = DateEvents.objects.all()
    serializer_class = DateEventSerializer


class DateEventPlaceViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = DateEventPlaces.objects.all()
    serializer_class = DateEventPlaceSerializer


class PlannerListCreateAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer


class PlannerDetailAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer