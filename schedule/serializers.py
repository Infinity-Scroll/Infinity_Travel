# serializers.py
from rest_framework import serializers
from .models import Planners, PeriodEvents, DateEvents, DateEventPlaces

class DateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEvents
        fields = '__all__'

class PeriodEventSerializer(serializers.ModelSerializer):
    date_events = DateEventSerializer(many=True, read_only=True)

    class Meta:
        model = PeriodEvents
        fields = '__all__'

class PlannerSerializer(serializers.ModelSerializer):
    period_events = PeriodEventSerializer(many=True, read_only=True)

    class Meta:
        model = Planners
        fields = '__all__'
        
class DateEventPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEventPlaces
        fields = '__all__'
