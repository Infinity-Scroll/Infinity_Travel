# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자만이 수정 및 삭제할 수 있는 권한을 부여합니다.
    """
    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 객체의 소유자에게만 허용
        return obj.owner == request.user

class IsOwnerOrReadOnlySchedule(IsOwnerOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return obj.owner == request.user

class IsOwnerOrReadOnlyPeriodEvent(IsOwnerOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return obj.schedule.owner == request.user

class IsOwnerOrReadOnlyDateEvent(IsOwnerOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return obj.period_event.schedule.owner == request.user
