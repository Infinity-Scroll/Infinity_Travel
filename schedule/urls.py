# schedule/urls.py

from django.urls import path
from .views import (
    PlannerListCreateAPIView, PlannerDetailAPIView,
    PeriodEventListCreateAPIView, PeriodEventDetailAPIView,
    DateEventListCreateAPIView, DateEventDetailAPIView, PlannerListAPIView,
    PlannerCreateAPIView, PeriodEventCreateAPIView, DateEventCreateAPIView,
    PlannerEditAPIView, PlannerDeleteAPIView, PeriodEventEditAPIView,
    PeriodEventDeleteAPIView, DateEventEditAPIView, DateEventDeleteAPIView
)

urlpatterns = [
    path('planner/create/', PlannerCreateAPIView.as_view(), name='planner-create'),
    path('planner/list-create/', PlannerListCreateAPIView.as_view(), name='planner-list-create'),
    path('planner/<int:pk>/', PlannerDetailAPIView.as_view(), name='planner-detail'),
    path('planner/edit/<int:pk>/', PlannerEditAPIView.as_view(), name='planner-edit'),
    path('planner/delete/<int:pk>/', PlannerDeleteAPIView.as_view(), name='planner-delete'),

    path('period-event/create/', PeriodEventCreateAPIView.as_view(), name='period-event-create'),
    path('period-event/list-create/', PeriodEventListCreateAPIView.as_view(), name='period-event-list-create'),
    path('period-event/<int:pk>/', PeriodEventDetailAPIView.as_view(), name='period-event-detail'),
    path('period-event/edit/<int:pk>/', PeriodEventEditAPIView.as_view(), name='period-event-edit'),
    path('period-event/delete/<int:pk>/', PeriodEventDeleteAPIView.as_view(), name='period-event-delete'),

    path('date-event/create/', DateEventCreateAPIView.as_view(), name='date-event-create'),
    path('date-event/list-create/', DateEventListCreateAPIView.as_view(), name='date-event-list-create'),
    path('date-event/<int:pk>/', DateEventDetailAPIView.as_view(), name='date-event-detail'),
    path('date-event/edit/<int:pk>/', DateEventEditAPIView.as_view(), name='date-event-edit'),
    path('date-event/delete/<int:pk>/', DateEventDeleteAPIView.as_view(), name='date-event-delete'),
    
    path('plannerList/', PlannerListAPIView.as_view(), name='planner-list'),

]

