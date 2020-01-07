from rest_framework import serializers
# For converting input data into python objects and vice versa
from profiles__api import models


class HelloAPIViewSerializer(serializers.Serializer):
    """Serialize a name field for testing our HelloAPIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
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
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItems
        fields = ('id', 'user_profile', 'status_text', 'created_on', 'updated_at')
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> feed_items relation can only be read
