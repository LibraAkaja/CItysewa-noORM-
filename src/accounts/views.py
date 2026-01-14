from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)

from .serializers import (
    CustomerRegisterSerializer,
)


class CustomerRegisterAPIView(APIView):
    # authentication_classes = []
    # permission_classes = []
    
    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)        
        if serializer.is_valid():
            data = serializer.save()
            print("IN view:\n", data)
            return Response(data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)