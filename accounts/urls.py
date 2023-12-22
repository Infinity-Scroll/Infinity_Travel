from django.urls import path
from .views import *

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="tokenrefresh"),
    path(
        "verify-email/<str:uidb64>/<str:token>/",
        EmailVerificationView.as_view(),
        name="verify-email",
    ),
    path("", UserAPIView.as_view(), name="user"),
]
