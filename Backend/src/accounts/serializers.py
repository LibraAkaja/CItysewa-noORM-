from rest_framework import serializers
from django.contrib.auth import authenticate

from .tables import (
    User,
    Token,
    Customer,
    Provider,
    Documents,
)
from .constants import (
    USER_ALREADY_EXISTS,
    CUSTOMER_PROFILE_EXISTS,
    PROVIDER_PROFILE_EXISTS,
    INVALID_PASSWORD,
    USER_NOT_FOUND,
    CUSTOMER_PROFILE_DOES_NOT_EXIST,
    PROVIDER_PROFILE_DOES_NOT_EXIST,
    ADMIN_ACCESS_DENIED
)

# Admin serializers
# ----------------------------------------------------------------------------------------------------------

class AdminRegisterSeriaizer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    def validate(self, attrs):
        email = attrs.get("email")
        user = User().get(email=email)
        if user:
            raise serializers.ValidationError({
                "message": USER_ALREADY_EXISTS
            })
            
        return attrs
    
    def create(self, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        user = User().create(email=email, password=password, is_admin=True)
        response = user.__dict__
        response.pop("password")        
        return user.__dict__
       
       
class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User().get(email=email)
        
        if user:
            if not user.is_admin:
                raise serializers.ValidationError({
                    "message": ADMIN_ACCESS_DENIED
                })
            if not user.check_password(password):
                raise serializers.ValidationError({
                    "message": INVALID_PASSWORD
                })
        
        else:
            raise serializers.ValidationError({
                "message": USER_NOT_FOUND
            })
            
        attrs["user_id"] = user.id
        return attrs       
        
        
    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        token = Token().get(user_id=user_id)
        
        if not token:
            token = Token().create(user_id=user_id)
                    
        user = User().get(id=user_id)
        user_details = user.__dict__
        user_details.pop("password")
        return {**user_details, "token": token.token}
            
        

# Customer serializers
# ----------------------------------------------------------------------------------------------------------

class CustomerRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User().get(email=email)
        if user:
            user_id = user.id
            customer_profile = Customer().get(user_id=user_id)
            if customer_profile:
                raise serializers.ValidationError({
                    "message": CUSTOMER_PROFILE_EXISTS
                })
            if not user.check_password(password):
                raise serializers.ValidationError({"message": INVALID_PASSWORD})            
            
            attrs["user_id"] = user_id   
        
        return attrs
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        
        if not user_id:
            user = User().create(email=email, password=password)
            user_id = user.id
          
        return {"email": email, **Customer().create(user_id=user_id, **validated_data).__dict__}
        
        
class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User().get(email=email)
        
        if user:
            customer_profile = Customer().get(user_id=user.id)
            if customer_profile:
                if not user.check_password(password):
                    raise serializers.ValidationError({
                        "message": INVALID_PASSWORD
                    })
            else:
                raise serializers.ValidationError({
                    "message": CUSTOMER_PROFILE_DOES_NOT_EXIST
                })
                    
        else:
            raise serializers.ValidationError({
                "message": USER_NOT_FOUND
            })
            
        attrs["user_id"] = user.id
        attrs["customer"] = customer_profile
        return attrs
    
    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        token = Token().get(user_id=user_id)
        
        if not token:
            token = Token().create(user_id=user_id)
                    
        customer = validated_data.get("customer")
        return {**customer.__dict__, "token": token.token}
        
    
class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()

    
# Provider serializers
# ----------------------------------------------------------------------------------------------------------

class ProviderRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User().get(email=email)
        if user:
            user_id = user.id
            provider_profile = Provider().get(user_id=user_id)
            if provider_profile:
                raise serializers.ValidationError({
                    "message": PROVIDER_PROFILE_EXISTS
                })
            if not user.check_password(password):
                raise serializers.ValidationError({"message": INVALID_PASSWORD})            
            
            attrs["user_id"] = user_id   
        
        return attrs
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        
        if not user_id:
            user = User().create(email=email, password=password)
            user_id = user.id
          
        return {"email": email, **Provider().create(user_id=user_id, **validated_data).__dict__}
        
        
class ProviderLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User().get(email=email)
        
        if user:
            provider_profile = Provider().get(user_id=user.id)
            if provider_profile:
                if not user.check_password(password):
                    raise serializers.ValidationError({
                        "message": INVALID_PASSWORD
                    })
            else:
                raise serializers.ValidationError({
                    "message": PROVIDER_PROFILE_DOES_NOT_EXIST
                })
                    
        else:
            raise serializers.ValidationError({
                "message": USER_NOT_FOUND
            })
            
        attrs["user_id"] = user.id
        attrs["provider"] = provider_profile
        return attrs
    
    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        token = Token().get(user_id=user_id)
        
        if not token:
            token = Token().create(user_id=user_id)
                    
        provider = validated_data.get("provider")
        return {**provider.__dict__, "token": token.token}
        
    
class ProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    
class DocumentSerializer(serializers.Serializer):
    provider_id = serializers.IntegerField(required=True)
    document_number = serializers.CharField(required=True)
    document_type = serializers.CharField(required=True)
    file = serializers.ImageField(required=True)
    
class ProviderVerificationSerializer(serializers.Serializer):
    provider_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    phone_number = serializers.CharField(required=True)
    document_type = serializers.CharField(required=True)
    document_number = serializers.CharField(required=True)
    profile_photo = serializers.ImageField(required=True)
    file = serializers.ImageField(required=True)
    
    def validate(self, attrs):
        ...
        
    def create(self, validated_data):
        ...
    