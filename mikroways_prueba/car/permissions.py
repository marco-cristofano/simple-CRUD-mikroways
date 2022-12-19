from rest_framework import permissions


class CarPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ('all_delete_with_permission', ):
            return request.user.has_perm('car.can_delete_all_whit_permission')
        return True

    def has_object_permission(self, request, view, obj):
        return True
