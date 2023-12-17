# views.py
from rest_framework import generics
from .permissions import IsOwnerOrReadOnlySchedule, IsOwnerOrReadOnlyPeriodEvent, IsOwnerOrReadOnlyDateEvent
from .models import Planner, PeriodEvent, DateEvent
from .serializers import PlannerSerializer, PeriodEventSerializer, DateEventSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class PlannerListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer
    permission_classes = [AllowAny]

class PlannerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnlySchedule]
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer
    permission_classes = [AllowAny]
    
# 일정 리스트
class PlannerListAPIView(generics.ListAPIView):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer    
    permission_classes = [AllowAny]

class PlannerCreateAPIView(generics.CreateAPIView):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer
    permission_classes = [AllowAny]
    
class PlannerEditAPIView(generics.UpdateAPIView):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer
    
# Planner 삭제 뷰
class PlannerDeleteAPIView(generics.DestroyAPIView):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer    





# Period Event 


class PeriodEventListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = PeriodEvent.objects.all()
    serializer_class = PeriodEventSerializer

class PeriodEventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = PeriodEvent.objects.all()
    serializer_class = PeriodEventSerializer

class PeriodEventCreateAPIView(generics.CreateAPIView):
    queryset = PeriodEvent.objects.all()
    serializer_class = PeriodEventSerializer
    permission_classes = [AllowAny]

# Period Event 수정 뷰
class PeriodEventEditAPIView(generics.UpdateAPIView):
    queryset = PeriodEvent.objects.all()
    serializer_class = PeriodEventSerializer

# Period Event 삭제 뷰
class PeriodEventDeleteAPIView(generics.DestroyAPIView):
    queryset = PeriodEvent.objects.all()
    serializer_class = PeriodEventSerializer






# DateEvent 

class DateEventListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = DateEvent.objects.all()
    serializer_class = DateEventSerializer

class DateEventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = DateEvent.objects.all()
    serializer_class = DateEventSerializer
    
class DateEventCreateAPIView(generics.CreateAPIView):
    queryset = DateEvent.objects.all()
    serializer_class = DateEventSerializer
    permission_classes = [AllowAny]   

# Date Event 수정 뷰
class DateEventEditAPIView(generics.UpdateAPIView):
    queryset = DateEvent.objects.all()
    serializer_class = DateEventSerializer

# Date Event 삭제 뷰
class DateEventDeleteAPIView(generics.DestroyAPIView):
    queryset = DateEvent.objects.all()
    serializer_class = DateEventSerializer



