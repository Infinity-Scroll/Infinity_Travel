from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import AccessToken


from rest_framework.permissions import IsAuthenticated


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["HEAD", "OPTIONS"]:
            return True

        return obj.user == request.user


class JWTCookieAuthenticated(BasePermission):
    def has_permission(self, request, view):
        cookie = request.COOKIES.get("access_token")

        if not cookie:
            return False

        try:
            access_token = AccessToken(cookie)
        except:
            return False

        return True


def get_user_id(request):
    token = AccessToken(request.COOKIES.get("access_token"))
    user_id = token.payload["user_id"]
    return user_id
