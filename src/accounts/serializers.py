from rest_framework import serializers


from .tables import (
    Users,
    Customers,
)
from .constants import (
    CUSTOMER_PROFILE_EXISTS,
    PROVIDER_PROFILE_EXISTS
)



class CustomerRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        user = Users().get({"email":email})
        if user:
            user_id = user[0]
            customer_profile = Customers().get({"id": user_id})
            if customer_profile:
                raise serializers.ValidationError({
                    "message": CUSTOMER_PROFILE_EXISTS
                })
            
            attrs["user_id"] = user_id   
        
        return attrs
    
    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        
        if not user_id:
            values = {'email': email, 'password': password}
            Users().create(values=values)
            user_id = Users().get({"email":email})[0]
          
        Customers().create(validated_data)
        return validated_data
        