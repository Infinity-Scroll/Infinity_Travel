from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PlaceViewSet, CommentViewSet, search_places

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('search-places/', search_places, name='search-places'),
]

'''
Comment 생성 (POST): /api/comments/
Comment 목록 조회 (GET): /api/comments/
특정 Comment 조회 (GET): /api/comments/<comment_id>/
특정 Comment 수정 (PUT or PATCH): /api/comments/<comment_id>/
특정 Comment 삭제 (DELETE): /api/comments/<comment_id>/
'''