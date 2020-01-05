from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles__api import Serializer
from rest_framework import viewsets

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = Serializer.HelloAPIViewSerializer

    def get(self, request, formate=None):
        """Test get API View"""
        an_apiview = ['Hi! There', 'How you doin', 'I am', 'Great!!!' ]
        return Response({'APIView': 'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello',{name}
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, pk=None):
        """Handling an Object"""
        return Response({'Method': 'POST'})

    def patch(self, request, pk=None):
        """Handling a partial update of the Object"""
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an Object"""
        return Response({'Method': 'DELETE'})


class HelloAPIViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = Serializer.HelloAPIViewSerializer

    def list(self, request, formate=None):
        """Test get API View"""
        an_apiviewset = ['Hi! There', 'How you doin', 'I am', 'Great!!!' ]
        return Response({'APIViewSet': 'Hello', 'an_apiview':an_apiviewset})

    def create(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello',{name}
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
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
