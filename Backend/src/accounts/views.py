from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from drf_spectacular.utils import extend_schema

from .tables import (
    Customer,
    Provider
)

from .serializers import (
    AdminRegisterSeriaizer,
    AdminLoginSerializer,
    CustomerRegisterSerializer,
    CustomerLoginSerializer,
    CustomerSerializer,
    ProviderRegisterSerializer,
    ProviderLoginSerializer,
    ProviderSerializer
)

# Admin views
# -----------------------------------------------------------------------------------------

class AdminRegisterAPIView(APIView):
    def post(self, request):
        serializer = AdminRegisterSeriaizer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AdminLoginAPIView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# Customer views
# ----------------------------------------------------------------------------------------- 

class CustomerRegisterAPIView(APIView):    
    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)        
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class CustomerLoginAPIView(APIView):
    def post(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
   

@extend_schema(
    summary="List all customers",
    description="Returns a lits of all customers",
    operation_id="customer_list"
)   
class CustomerListAPIView(APIView):
    def get(self, request):
        customers = Customer().all()
        serializer = CustomerSerializer(customers, many=True)        
        return Response(serializer.data, status=HTTP_200_OK) 

@extend_schema(
    summary="Retrive a customer details",
    description="Returns details of customer using their id.",
    operation_id='customer_detail'
)   
class CustomerRetrieveAPIView(APIView):
    def get(self, request, id):
        customer = Customer().get(id=id)
        if customer:
            serializer = CustomerSerializer(customer.__dict__)        
            return Response(serializer.data, status=HTTP_200_OK)
                     
        return Response({"detail": "Not found"}, status=HTTP_404_NOT_FOUND)
    
        
# Provider views
# -----------------------------------------------------------------------------------------

class ProviderRegisterAPIView(APIView):    
    def post(self, request):
        serializer = ProviderRegisterSerializer(data=request.data)        
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ProviderLoginAPIView(APIView):
    def post(self, request):
        serializer = ProviderLoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=HTTP_200_OK)        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
   

@extend_schema(
    summary="List all providers",
    description="Returns a lits of all customers",
    operation_id="provider_list"
)   
class ProviderListAPIView(APIView):
    def get(self, request):
        providers = Provider().all()
        serializer = ProviderSerializer(providers, many=True)        
        return Response(serializer.data, status=HTTP_200_OK) 

@extend_schema(
    summary="Retrive a provider details",
    description="Returns details of provider using their id.",
    operation_id='provider_detail'
)   
class ProviderRetrieveAPIView(APIView):
    def get(self, request, id):
        provider = Provider().get(id=id)
        if provider:
            serializer = ProviderSerializer(provider.__dict__)        
            return Response(serializer.data, status=HTTP_200_OK)
                     
        return Response({"detail": "Not found"}, status=HTTP_404_NOT_FOUND)