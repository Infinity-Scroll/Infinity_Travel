from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlannerViewSet, PeriodEventViewSet, DateEventViewSet, DateEventPlaceViewSet,PlannerListCreateAPIView, PlannerDetailAPIView,update_date_events

router = DefaultRouter()

router.register(r'planners', PlannerViewSet)
router.register(r'period-events', PeriodEventViewSet)
router.register(r'date-events', DateEventViewSet)
router.register(r'date-event-places', DateEventPlaceViewSet)  # DateEventPlaceViewSet 추가

urlpatterns = [
    path('api/', include(router.urls)),
    # 기존의 views를 위한 URL 패턴들
    path('api/planner/list-create/', PlannerListCreateAPIView.as_view(), name='planner-list-create'),
    path('api/planner/detail/<int:pk>/', PlannerDetailAPIView.as_view(), name='planner-detail'),
    path('update-date-events/', update_date_events, name='update_date_events')
]
