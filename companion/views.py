from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Companion
from .serializers import CompanionSerializer

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


class CompanionViewSet(viewsets.ModelViewSet):
    queryset = Companion.objects.all()
    serializer_class = CompanionSerializer
    permission_classes = [IsAuthenticated]


@ensure_csrf_cookie
def my_view(request):
    response = JsonResponse({'key': 'value'})
    response['Access-Control-Allow-Origin'] = '*'  # 이 부분을 요청하는 도메인에 맞게 수정
    return response