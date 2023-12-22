from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlannerViewSet, PeriodEventViewSet, DateEventViewSet, DateEventPlaceViewSet,PlannerListCreateAPIView, PlannerDetailAPIView

router = DefaultRouter()

router.register(r'planners', PlannerViewSet)
router.register(r'period-events', PeriodEventViewSet)
router.register(r'date-events', DateEventViewSet)
router.register(r'date-event-places', DateEventPlaceViewSet)  # DateEventPlaceViewSet 추가

urlpatterns = [
    path('api/', include(router.urls)),
    # 기존의 views를 위한 URL 패턴들
    path('api/planner/list-create/', PlannerListCreateAPIView.as_view(), name='planner-list-create'),
    path('api/planner/detail/<int:pk>/', PlannerDetailAPIView.as_view(), name='planner-detail')   
]

'''
Planner 
api/planners/                   List 및 Create
api/planners/<pk>/              Retrieve, Update, Destroy

PeriodEvent         
api/period-events/              List 및 Create
api/period-events/<pk>/         Retrieve, Update, Destroy

DateEvent  
api/date-events/                List 및 Create
api/date-events/<pk>/           Retrieve, Update, Destroy

DateEventPlace ( 연결 ) 
api/date-event-places/          List 및 Create
api/date-event-places/<pk>/     Retrieve, Update, Destroy

api/planner/list-create/
api/planner/detail/<int:pk>/

'''