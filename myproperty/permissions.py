from rest_framework import permissions


class UpdateOwnProperty(permissions.BasePermission):
    """"Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own property"""
        if request.method in permissions.SAFE_METHODS:  # e-g get and patch.  UNSAFE_METHODS: delete
            return True
        return obj.owner.id == request.user.id  # property owner id == current user id


class UpdateOwnPropertyImages(permissions.BasePermission):
    """"Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own property"""
        if request.method in permissions.SAFE_METHODS:  # e-g get and patch.  UNSAFE_METHODS: delete
            return True
        return obj.owner.id == obj.property.id == request.user.id
        # images of a property id == current user id == property id
