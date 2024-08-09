from rest_framework import permissions
from users.models import UserRoles


class IsActiveUser(permissions.BasePermission):
    """
    Разрешает доступ только активным пользователям.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_active


class IsAdminUser(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки,
     является ли пользователь администратором.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == UserRoles.ADMIN.value
