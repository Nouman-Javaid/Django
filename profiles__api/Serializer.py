from rest_framework import serializers
# For converting input data into python objects and vice versa

class HelloAPIViewSerializer(serializers.Serializer):
    """Serialize a name field for testing our HelloAPIView"""
    name = serializers.CharField(max_length=10)