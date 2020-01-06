from rest_framework import serializers
# For converting input data into python objects and vice versa
from profiles__api import models


class HelloAPIViewSerializer(serializers.Serializer):
    """Serialize a name field for testing our HelloAPIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile objecc"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,     #Cannot search someone by reading password
                'style':{
                    'input_type': 'password'    #Only dottted characters
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        return user