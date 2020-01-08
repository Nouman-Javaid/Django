from rest_framework import serializers
from myproperty import models


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItems
        fields = ('id', 'user_profile', 'status_text', 'created_on', 'updated_at')
        extra_kwargs = {'user_profile': {'read_only': True}}  # Profile <-> feed_items relation can only be read
