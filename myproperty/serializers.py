from rest_framework import serializers
from myproperty import models

'''
class BasicPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicProperties
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> BasicProperty relation can only be read
'''


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> PropertyFeature relation can only be read


class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PropertyImages
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> PropertyImages relation can only be read




''' 
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItems
        fields = ('id', 'user_profile', 'status_text', 'created_on', 'updated_at')
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> feed_items relation can only be read
'''