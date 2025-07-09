from rest_framework import permissions


class IsRestaurantOwner(permissions.BasePermission):
    message = 'YOU DO NOT HAVE PERMISSIONS TO UPDATE THIS RESERVATION'

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user
    
class IsRestaurantOwnerOrReadOnly(permissions.BasePermission.has_object_permission):
    message = 'YOU DO NOT HAVE PERMISSION'
    def has_permission(self, request, view):
        if not request.user.has_object_permission():
            return super().has_permission(request, view)
    pass