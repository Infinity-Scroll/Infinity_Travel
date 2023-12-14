from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanionViewSet

router = DefaultRouter()
router.register(r'models', CompanionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]