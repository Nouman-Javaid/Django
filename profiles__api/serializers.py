# For converting input data into python objects and vice versa
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from profiles__api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'fullname', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # No one read or search someone by password
                'style': {
                    'input_type': 'password'  # Only dotted characters
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['fullname'],
            password=validated_data['password'],
        )
        return user


''' 
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItems
        fields = ('id', 'user_profile', 'status_text', 'created_on', 'updated_at')
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> feed_items relation can only be read
'''


class UserLoginSerialzer(serializers.Serializer):
    """Allow user to login"""
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        username = data.get('email', None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide valid email and password"
            raise exceptions.ValidationError(msg)
        return data


class HelloAPIViewSerializer(serializers.Serializer):
    """Serialize a name field for testing our HelloAPIView"""
    name = serializers.CharField(max_length=10)
