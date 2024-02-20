from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to modify data, but allow read-only access for all users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only access for all users
            return True
        else:
            # Modify operations require admin status
            return request.user and request.user.is_staff
