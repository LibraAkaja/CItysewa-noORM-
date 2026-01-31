import secrets

from django.contrib.auth.hashers import make_password, check_password

from src.core.db_manager import Table
from src.utils.storage import Storage

class Token(Table):
    table_name = 'tokens'
    _attrs = {
        "user_id": int,
        "token": str,        
    }
    required_fields = ["user_id", "token"]
    
    def __init__(self):
        self._attrs.update(super()._attrs)
        super().__init__()
        
    @staticmethod 
    def abstract_method():
        pass
    
    def create(self, user_id):
        token = self.generate_token()
        return super().create(user_id=user_id, token=token)
        
        
    def generate_token(self, length=40):
        """
        1 byte = 2 hex-digits. So for 20 bytes, it would be equal to 40 hex digits.
        """
        return secrets.token_hex(length//2)
    

class User(Table):
    table_name = 'users'
    _attrs = {
        "email": str,
        "phone_number": str,
        "password": str,
        "is_admin": bool,
        "is_active": bool,
    }
    required_fields = ['email', 'password']
        
    def __init__(self):
        self._attrs.update(super()._attrs)        
        super().__init__()        
       
    @staticmethod 
    def abstract_method():
        pass
    
    def create(self, **kwargs):
        raw_password = kwargs.pop("password", None)
        if raw_password:
            password_hash = self.set_password(raw_password)
        else:
            raise ValueError("Password is required.")
        
        kwargs["password"] = password_hash
        return super().create(**kwargs)
    
    def update(self, **kwargs):
        if "password" in kwargs:
            raw_password = kwargs.pop("password")
            password_hash = self.set_password(raw_password)
            kwargs["password"] = password_hash
            
        return super().update(**kwargs)
    
    def set_password(self, password):
        self.password = make_password(password)
        return self.password
    
    def check_password(self, raw_password):
        password = self.password
        return check_password(raw_password, password)   
    
class Customer(Table):
    table_name = 'customers'
    _attrs = {
        "user_id": int,
        "first_name": str,
        "last_name": str,
        "gender": str,
        "photo": str
    }
    required_fields = ['user_id']
    
    def __init__(self):
        self._attrs.update(super()._attrs)
        super().__init__()
       
    @staticmethod 
    def abstract_method():
        pass
    
    def upload_photo(self, file):
        if hasattr(self, "id"): 
            file_name = Storage().upload_file(
                bucket="customer", 
                folder=f"photos/{self.id}",
                file=file
            )
            return file_name
        else:
            raise ValueError("Id missing for this instance.") 
    
    def delete_photo(self):
        if hasattr(self, "photo"):
            Storage().delete_file(bucket="customer", folder=f"photos/{self.id}", file_name=self.photo)
            
class Provider(Table):
    table_name = 'providers'
    _attrs = {
        "user_id": int,
        "first_name": str,
        "last_name": str,
        "gender": str,
        "description": str,
        "photo": str,
        "verified": bool
    }
    required_fields = ['user_id']
    
    def __init__(self):
        self._attrs.update(super()._attrs)
        super().__init__()
       
    @staticmethod 
    def abstract_method():
        pass
    
    def upload_photo(self, file):
        if hasattr(self, "id"): 
            file_name = Storage().upload_file(
                bucket="provider", 
                folder=f"photos/{self.id}",
                file=file
            )
            return file_name
        else:
            raise ValueError("Id missing for this instance.") 
        
    def get_photo_url(self, id:int, photo_name:str):
        photo_url =Storage().get_file_link(bucket='provider', file_path=f'photos/{id}/{photo_name}')
        return photo_url
        
    def delete_photo(self):
        if hasattr(self, "photo"):
            Storage().delete_file(bucket="provider", folder=f"photos/{self.id}", file_name=self.photo)
        
class Document(Table):
    table_name = 'documents'
    _attrs = {
        "provider_id": int,
        "document_type": str,
        "document_number": str,
        "file_name": str,
        "status": str,
    }
    required_fields = ['provider_id', 'document_type', 'document_number', 'file_name']
    
    def __init__(self):
        self._attrs.update(super()._attrs)
        super().__init__()
       
    @staticmethod 
    def abstract_method():
        pass
    
    def upload_file(self, provider_id:int, file):
        file_name = Storage().upload_file(
                bucket="provider", 
                folder=f"documents/{provider_id}",
                file=file
            )
        return file_name    
    
    def get_file_url(self, provider_id:int, file_name):
        document_url =Storage().get_file_link(bucket='provider', file_path=f'documents/{provider_id}/{file_name}')
        return document_url         

if __name__ == "__main__":
    print(User().all())
    