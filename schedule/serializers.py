from rest_framework import serializers
from .models import Planners, PeriodEvents, DateEvents, DateEventPlaces
from place.serializers import PlaceSerializer
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer

class DateEventPlaceSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()  # Assuming you have a PlaceSerializer

    class Meta:
        model = DateEventPlaces
        fields = ['order', 'place']

class DateEventSerializer(serializers.ModelSerializer):
    date_event_places = DateEventPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = DateEvents
        fields = ['event_date', 'date_event_places']

class PeriodEventSerializer(serializers.ModelSerializer):
    date_events = DateEventSerializer(many=True, read_only=True)

    class Meta:
        model = PeriodEvents
        fields = ['name', 'start_date', 'end_date', 'date_events']
        
class PlannerSerializer(serializers.ModelSerializer):
    period_events = PeriodEventSerializer(many=True, read_only=True)
    user_image_url = serializers.ImageField(source='user.profile.image_url', read_only=True)
    user_pk = serializers.IntegerField(source='user.pk', read_only=True)

    class Meta:
        model = Planners
        fields = ['name', 'start_date', 'end_date', 'public_flag', 'area', 'period_events', 'user_image_url','user_pk']
