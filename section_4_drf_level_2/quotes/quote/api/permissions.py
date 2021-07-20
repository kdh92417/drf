from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):
        is_admin = super().has_object_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
