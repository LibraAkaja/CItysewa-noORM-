from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from drf_spectacular.utils import extend_schema

from .tables import (
    Customer,
    Provider,
    Document
)

from .serializers import (
    UserRegisterSeriaizer,
    AdminLoginSerializer,
    CustomerRegisterSerializer,
    CustomerLoginSerializer,
    CustomerSerializer,
    ProviderRegisterSerializer,
    ProviderLoginSerializer,
    ProviderSerializer,
    ProviderSubmitVerificationSerializer,
    VerificationListSerializer,
    VerificationRetrieveSerializer,
    VerificationPatchSerializer,
)


# Admin views
# -----------------------------------------------------------------------------------------

class AdminRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSeriaizer(data=request.data)
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
    
    
class ProviderSubmitVerificationAPIView(APIView):
    def post(self, request):
        serializer = ProviderSubmitVerificationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data=data, status=HTTP_200_OK)
            
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        
class VerificationListAPIView(APIView):
    def get(self, request):
        verification_status = request.query_params.get("status", 'Pending')
        verification_data = Provider().join(
            right_table=Document(),
            join_on=("id","provider_id"),
            left_attrs=("id", "first_name", "last_name", "gender"),
            right_attrs = ("document_number", "status",),
            left_conditions={},
            right_conditions={"status": verification_status}
            )
        
        # Removing the prefixes 'provider_' and 'document_' from keys eg: provider_column_name or
        transformed_data = []
        for item in verification_data:
            temp_dict = {}
            for key, val in item.items():
                new_key = key.removeprefix(f"{Provider.table_name}_")
                new_key = new_key.removeprefix(f"{Document.table_name}_")
                temp_dict[new_key] = val
            
            transformed_data.append(temp_dict)

        serializer = VerificationListSerializer(transformed_data, many=True)
        
        return Response(serializer.data, status=HTTP_200_OK)
    
class VerificationRetrieveAPIView(APIView):
    def get(self, request, id):
        verification_data = Provider().join(
            right_table=Document(),
            join_on=("id","provider_id"),
            left_attrs=("id", "first_name", "last_name", "gender", "photo", "verified"),
            right_attrs = ("document_type", "document_number", "file_name", "status"),
            left_conditions={"id":id},
            right_conditions={"status": 'Pending'}
            )
        
        # Removing the prefixes 'provider_' and 'document_' from keys eg: provider_column_name or
        transformed_data = {}
        for key, val in verification_data[0].items():
                new_key = key.removeprefix(f"{Provider.table_name}_")
                new_key = new_key.removeprefix(f"{Document.table_name}_")
                transformed_data[new_key] = val
                
        transformed_data["photo"] = Provider().get_photo_url(id=transformed_data["id"], photo_name=transformed_data["photo"])
        transformed_data["file_name"] = Document().get_file_url(provider_id=transformed_data["id"], file_name=transformed_data["file_name"])
        serializer = VerificationRetrieveSerializer(transformed_data)
        
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, id):
        provider_id = id
        serializer = VerificationPatchSerializer(data=request.data, instance={"id": provider_id})
        if serializer.is_valid():
            data = serializer.save()
            return Response(data=data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)