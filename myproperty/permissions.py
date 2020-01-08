from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """"Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:  # e-g get and patch.  UNSAFE_METHODS: delete
            return True
        return obj.id == request.user.id  # Requesting user and updating object have same id's