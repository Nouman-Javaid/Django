from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from myproperty import permissions, serializers, models
from myproperty.models import PropertyImages


class PropertyViewSet(viewsets.ModelViewSet):
    """ A viewSet for viewing and editing user instances. """

    serializer_class = serializers.PropertySerializer
    queryset = models.Property.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (permissions.UpdateOwnProperty,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save()


class PropertyImagesViewSet(viewsets.ModelViewSet):
    """ A viewSet for viewing and editing user instances. """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (permissions.UpdateOwnPropertyImages, )
    queryset = models.PropertyImages.objects.all()
    serializer_class = serializers.PropertyImagesSerializer

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        obj = serializer.save()
        for f in self.request.data.getlist('files'):
            mf = PropertyImages.objects.create(file=f)
            obj.files.add(mf)


'''
class BasicPropertiesViewSet(viewsets.ModelViewSet):
    """ A viewset for viewing and editing user instances. """
    serializer_class = serializers.BasicPropertiesSerializer
    queryset = models.BasicProperties.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (permissions.UpdateOwnProperty, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile  to the logged in user"""
        serializer.save(user_profile=self.request.user)
'''





'''
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
'''