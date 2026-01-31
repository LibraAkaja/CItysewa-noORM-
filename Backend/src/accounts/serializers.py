from rest_framework import serializers
# from django.contrib.auth import authenticate

from src.utils.storage import Storage
from .tables import (
    User,
    Token,
    Customer,
    Provider,
    Document,
)
from .messages import (
    USER_ALREADY_EXISTS,
    CUSTOMER_PROFILE_EXISTS,
    PROVIDER_PROFILE_EXISTS,
    INVALID_PASSWORD,
    USER_NOT_FOUND,
    CUSTOMER_NOT_FOUND,
    DOCUMENT_NOT_FOUND,
    PROVIDER_NOT_FOUND,
    CUSTOMER_PROFILE_DOES_NOT_EXIST,
    PROVIDER_PROFILE_DOES_NOT_EXIST,
    ADMIN_ACCESS_DENIED,
    INVALID_DOCUMENT_TYPE,
    PHONE_NUMBER_ALREADY_ASSOCIATED,
    EMAIL_ALREADY_ASSOCIATED,
    DOCUMENT_ASSOCIATED_WITH_ANOTHER_ACC,
)

from .validators import (
    validate_file_size,
    validate_phone_number
)

from .constants import (
    DOCUMENT_TYPE
)

# User serializers
# ----------------------------------------------------------------------------------------------------------

class UserRegisterSeriaizer(serializers.Serializer):
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
        user.__dict__.pop("password")    
        return user.__dict__
   
class UserPatchSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=False, validators=[validate_phone_number])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False, default=True)
    is_admin = serializers.BooleanField(required=False)
    
    def validate(self, attrs):
        user_id = self.instance["id"]
        user = User().get(id=user_id)
        if user:
            if phone_number:=attrs.get("phone_number"):
                user_exist = User().get(phone_number = phone_number)
                if user_exist:
                    if user_id != user_exist.id:
                        raise serializers.ValidationError({
                            "message": PHONE_NUMBER_ALREADY_ASSOCIATED
                        })
            if email:=attrs.get("email"):
                user_exist = User().get(email = email)
                if user_id != user_exist.id:
                    raise serializers.ValidationError({
                        "message": EMAIL_ALREADY_ASSOCIATED
                    })
        else:
            raise serializers.ValidationError({
                "message": USER_NOT_FOUND
            })            
        return attrs
    
    def update(self, instance, validated_data):
        user_id =  instance["id"]
        User().update(id=user_id, **validated_data)
        updated_user = User().get(id=user_id)
        updated_user.__dict__.pop("password")
        return {**updated_user.__dict__}
        
    
# Admin serializers
# ----------------------------------------------------------------------------------------------------------
      
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
    password = serializers.CharField(required=True)
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

class ProviderPatchSerializer(serializers.Serializer):
    ...       
        
class ProviderLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    
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
    
class DocumentCreateSerializer(serializers.Serializer):
    provider_id = serializers.IntegerField(required=True)
    document_number = serializers.CharField(required=True)
    document_type = serializers.CharField(required=True)
    file = serializers.FileField(required=True, validators=[validate_file_size])
    
    def validate(self, attrs):
        provider_id = attrs.get("provider_id")
        document_number = attrs.get("document_number")
        document = Document().get(document_number=document_number)
        if document:
            if provider_id != document.provider_id:
                raise serializers.ValidationError({
                    "message": DOCUMENT_ASSOCIATED_WITH_ANOTHER_ACC
                })
            else:
                attrs["document"] = document
                
        return attrs
    
    def create(self, validated_data):     
        document = validated_data.pop("document", None)       
        if document is None:                             
            provider_id = validated_data.get("provider_id")      
            file = validated_data.pop("file", None)
            file_name = Document().upload_file(provider_id, file)
            validated_data["file_name"] = file_name
            document = Document().create(**validated_data)
            
        return {**document.__dict__}
    
class ProviderSubmitVerificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    phone_number = serializers.CharField(required=True, validators = [validate_phone_number])
    document_type = serializers.CharField(required=True)
    document_number = serializers.CharField(required=True)
    photo = serializers.ImageField(required=True, validators = [validate_file_size])
    document = serializers.FileField(required=True,  validators = [validate_file_size])
    
    def validate(self, attrs):
        document_type = attrs.get("document_type")
        
        if document_type not in DOCUMENT_TYPE:
            raise serializers.ValidationError({
                "message": INVALID_DOCUMENT_TYPE
            })
            
        id = attrs.get("id")
        provider = Provider().get(id=id)
        if not provider:
            raise serializers.ValidationError({
                "message": PROVIDER_PROFILE_DOES_NOT_EXIST
            })
            
        attrs["provider"] = provider
        return attrs
       
    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        photo = validated_data.get("photo")
        document = validated_data.get("document")
        document_number = validated_data.get("document_number")
        document_type = validated_data.get("document_type")
        
        provider = validated_data.get("provider")
        
        user_serializer = UserPatchSerializer(
            instance={"id": provider.user_id},
            data={"phone_number":phone_number},
            partial=True
            )
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
        
        document_serialzier = DocumentCreateSerializer(
            data={
                "provider_id": provider.id,
                "document_number": document_number,
                "document_type": document_type,
                "file": document
            }
        )
        if document_serialzier.is_valid(raise_exception=True):
            document_serialzier.save()
        
        if hasattr(provider, "photo"):
            provider.delete_photo()
        photo_name = provider.upload_photo(photo)
        provider.update(id=provider.id, photo=photo_name)
        
        return {"phone_number": phone_number, "document_number": document_number}
        
class VerificationListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    document_number = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    
class VerificationRetrieveSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    photo = serializers.CharField(required=True)
    verified = serializers.BooleanField(required=True)
    document_type = serializers.CharField(required=True)
    document_number = serializers.CharField(required=True)
    file_name = serializers.CharField(required=True)
    status = serializers.CharField(required=True)

    
class VerificationPatchSerializer(serializers.Serializer):
    verified = serializers.BooleanField(required=True)
    document_number = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
   
    def validate(self, attrs):
        provider_id = self.instance["id"]
        provider = Provider().get(id=provider_id)
        if provider:            
            document_number  = attrs.get("document_number")
            document = Document().get(document_number=document_number)
            if not document:
                raise serializers.ValidationError({
                    "message": DOCUMENT_NOT_FOUND,
                })    
        else:
            raise serializers.ValidationError({
                "message": PROVIDER_NOT_FOUND
            })    
             
        attrs["document_id"] = document.id      
        return attrs
    
    def update(self, instance, validated_data):
        provider_id =  instance.get("id")
        document_id = validated_data.get("document_id")
        verified = validated_data.get("verified")
        document_status = validated_data.get("status")
        
        Provider().update(id=provider_id, verified=verified)
        Document().update(id=document_id, status=document_status)
        
        updated_provider = Provider().get(id=provider_id)
        
        return {
            "id": updated_provider.id,
            "first_name": updated_provider.first_name,
            "last_name": updated_provider.last_name,
            "verified": updated_provider.verified
            }