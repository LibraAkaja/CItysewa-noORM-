from django.contrib.auth.hashers import make_password, check_password

from src.core.db_manager import Table


class User(Table):
    table_name = 'users'
    _attrs = {
        "email": str,
        "phone_number": str,
        "password": str | None,
        "is_admin": bool,
        "is_active": bool,
    }
    required_fields = ['email', 'password']
        
    def __init__(self):
        super().__init__()
        self._attrs.update(super()._attrs)
       
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
    
    def set_password(self, password):
        self.password = make_password(password)
        return self.password
    
    def check_password(self, raw_password):
        password = self.password
        return check_password(raw_password, password)
    
    def __str__(self):
        return (f"Table instance: {self.table_name}")
    
    
class Customer(Table):
    table_name = 'customers'
    _attrs = {
        "user_id": int,
        "first_name": str,
        "last_name": str,
        "gender": str,
        "photo_url": bool
    }
    required_fields = ['user_id']
    
    def __init__(self):
        super().__init__()
        self._attrs.update(super()._attrs)
        self.first_name = 'No name'
       
    @staticmethod 
    def abstract_method():
        pass
        
    def __str__(self):
        return (f"Name: {self.first_name}")

if __name__ == "__main__":
    result = User().count(email="awe@test.com", is_active=True)
    print(result)