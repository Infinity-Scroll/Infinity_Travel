from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from core.permissions import get_user_id


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('companion/', include('companion.urls')),
    path("place/", include("place.urls")),
    path('schedule/', include('schedule.urls')),
    path("chat/", include("chat.urls")),
    path('get_user_id/', get_user_id, name='get_user_id'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

