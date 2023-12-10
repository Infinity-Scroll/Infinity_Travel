from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *


# router = DefaultRouter()
# router.register("accounts", User)

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="tokenrefresh"),
]
