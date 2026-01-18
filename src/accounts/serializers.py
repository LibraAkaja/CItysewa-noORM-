from rest_framework import serializers
from django.contrib.auth import authenticate

from .tables import (
    User,
    Customer,
)
from .constants import (
    USER_ALREADY_EXISTS,
    CUSTOMER_PROFILE_EXISTS,
    PROVIDER_PROFILE_EXISTS,
    INVALID_PASSWORD
)

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
        
        
class CustomerListSerializer(serializers.Serializer):
    ...
    
