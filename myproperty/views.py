from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.decorators import login_required
from myproperty import permissions, serializers, models


# Create your views here.
class UserProfileFeedAPI(viewsets.ModelViewSet):
    """Handle creat, update, delete and retrieve profile feed items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItems.objects.all()

    # @login_required
    def perform_create(self, serializer):
        """Sets the user profile  to the logged in user"""
        serializer.save(user_profile=self.request.user)
