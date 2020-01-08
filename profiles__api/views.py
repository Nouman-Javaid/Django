from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from profiles__api import models
from profiles__api import serializers
from profiles__api import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginAPIView(APIView):
    permissions_classes = [IsAuthenticated]
    serializer_class = serializers.UserLoginSerialzer

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerialzer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        # print("str(token.key)", str(token.key))
        return Response({
            'token': token.key,
            # 'user_id': user.pk,
            'email': user.email,

        })


class UserLogoutAPIView(APIView):
    """Handle destroying user authentication token"""

    def get(self, request):
        # simply delete the token to force a logout
        try:
            # print("str(token.key)", request.user.auth_token)
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        logout(request)
        msg = "Successfully logged out."
        return Response({"success": msg}, status=status.HTTP_200_OK)


''' 
class UserProfileFeedAPI(viewsets.ModelViewSet):
    """Handle creat, update, delete and retrieve profile feed items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItems.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile  to the logged in user"""
        serializer.save(user_profile=self.request.user)
'''


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloAPIViewSerializer

    def get(self, request, formate=None):
        """Test get API View"""
        an_apiview = ['Hi! There', 'How you doin', 'I am', 'Great!!!']
        return Response({'APIView': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello', {name}
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk=None):
        """Handling a partial update of the Object"""
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an Object"""
        return Response({'Method': 'DELETE'})


class HelloAPIViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.HelloAPIViewSerializer

    def list(self, request, formate=None):
        """Test get API View"""
        an_apiviewset = ['Hi! There', 'How you doin', 'I am', 'Great!!!']
        return Response({'APIViewSet': 'Hello', 'an_apiviewset': an_apiviewset})

    def create(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello', {name}
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handling getting an object by its ID"""
        return Response({'Method': 'PATCH'})

    def update(self, request, pk=None):
        """Handling updating an object by its ID"""
        return Response({'Method': 'UPDATE'})

    def destory(self, request, pk=None):
        """Handling deleting an object by its ID"""
        return Response({'Method': 'DELETE'})
