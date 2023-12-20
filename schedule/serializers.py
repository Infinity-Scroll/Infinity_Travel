# serializers.py
from rest_framework import serializers
from .models import Planner, PeriodEvent, DateEvent, DateEventPlace

class DateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEvent
        fields = '__all__'

class PeriodEventSerializer(serializers.ModelSerializer):
    date_events = DateEventSerializer(many=True, read_only=True)

    class Meta:
        model = PeriodEvent
        fields = '__all__'

class PlannerSerializer(serializers.ModelSerializer):
    period_events = PeriodEventSerializer(many=True, read_only=True)

    class Meta:
        model = Planner
        fields = '__all__'
        
class DateEventPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEventPlace
        fields = '__all__'
