from rest_framework import serializers
from .models import Planners, PeriodEvents, DateEvents, DateEventPlaces

class DateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEvents
        fields = ['name', 'start_date','end_date','public_flag','area','user']

class PeriodEventSerializer(serializers.ModelSerializer):
    date_events = DateEventSerializer(many=True, read_only=True)

    class Meta:
        model = PeriodEvents
        fields = ['planner','name','start_date','end_date']

class PlannerSerializer(serializers.ModelSerializer):
    period_events = PeriodEventSerializer(many=True, read_only=True)

    class Meta:
        model = Planners
        fields = ['period_event','event_date','place']
        
class DateEventPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEventPlaces
        fields = ['date_event','order','place']
