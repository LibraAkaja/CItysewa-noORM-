from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)

from .serializers import (
    AdminRegisterSeriaizer,
    CustomerRegisterSerializer,
)

class AdminRegisterAPIView(APIView):
    def post(self, request):
        serializer = AdminRegisterSeriaizer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class CustomerRegisterAPIView(APIView):    
    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)        
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)