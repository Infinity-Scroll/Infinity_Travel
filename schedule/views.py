from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=True, methods=['post'])
    def update_places(self, request, pk=None):
        date_event = self.get_object()
        place_ids = request.data.get('place_ids', [])
        
        # DateEventPlaces 업데이트
        DateEventPlaces.add_places_to_date_event(date_event, place_ids)

        return Response({'status': 'success'})
    

class DateEventPlaceViewSet(JWTCookieIsOwnerOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = DateEventPlaces.objects.all()
    serializer_class = DateEventPlaceSerializer


class PlannerListCreateAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer


class PlannerDetailAPIView(JWTCookieIsOwnerOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannerSerializer
    
    
@csrf_exempt
def update_date_events(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_places = data.get('selectedPlaces', '').split(',')
            date_event_id = data.get('dateEventId')

            date_event = DateEvents.objects.get(pk=date_event_id)

            date_event.place.clear()
            date_event.place.add(*selected_places)

            return JsonResponse({'message': 'DateEvent updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)