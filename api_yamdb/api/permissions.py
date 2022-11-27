from api import roles
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class CommonBasePermission(BasePermission):
    group_code = None

    def has_permission(self, request, view):
        user = request.user
        return (not user.is_anonymous
                and (user.is_superuser or user.role == self.group_code)
                )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (not user.is_anonymous
                and (user.is_superuser or user.role == self.group_code)
                )


class IsModerator(CommonBasePermission):
    group_code = roles.MODERATOR


class IsAdmin(CommonBasePermission):
    group_code = roles.ADMIN_GROUP


class AuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or obj.author == request.user)


class PermissionClassMixin(object):
    def get_permissions(self):
        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method

        if not hasattr(self, 'permission_action_classes'):
            return [permission() for permission in self.permission_classes]

        permissions = self.permission_action_classes.get(action)
        if permissions:
            return [permission() for permission in permissions]
        return [permission() for permission in self.permission_classes]
