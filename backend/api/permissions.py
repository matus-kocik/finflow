from rest_framework.permissions import BasePermission


class IsAuthenticatedAndOwner(BasePermission):
    """
    Permission class to check if the user is authenticated and is the owner of the object.

    This permission class ensures that the user making the request is authenticated and
    is the owner of the object being accessed.

    Methods:
        has_permission(request, view):
            Checks if the user is authenticated.
        has_object_permission(request, view, obj):
            Checks if the user is the owner of the object.
    """

    def has_permission(self, request, view):
        """Check if the user is authenticated."""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner of the object."""
        return obj.user == request.user
