from django.contrib.auth.hashers import make_password, check_password

from src.core.db_manager import Table


class Users(Table):
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
    
    def set_password(self, password):
        self.password = make_password(password)
        return self.password
    
    def check_password(self, raw_password):
        password = "fetch from database"
        return check_password(raw_password, password)
    
    def __str__(self):
        return (f"email: {self.email}")
    
    
class Customers(Table):
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
    result = Users().get(id='3')
    if result:
        print(result.__dict__)
    else:
        print(result)