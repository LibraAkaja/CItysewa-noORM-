from src.core.db_manager import Table


class Users(Table):
    table_name = 'users'
    required_fields = ['email', 'password']
    optional_fields = []
    foreign_key_fields = None
    
    def __init__(self):
        super().__init__()
        self.id = int()
        self.email = str()
        self.phone_number = str()
        self.password = str()
        self.is_admin = False
        self.is_active = True
        self.created_at = None
        self.updated_at = None
       
    @staticmethod 
    def abstract_table():
        pass
    
    def __str__(self):
        return (f"id: {self.id} email: {self.email}")
    
    
class Customers(Table):
    table_name = 'customers'
    required_fields = ['user_id']
    optional_fields = []
    foreign_key_fields = ['user_id']
    
    def __init__(self):
        super().__init__()
        self.id = int()
        self.user_id = int()
        self.first_name = str()
        self.last_name = str()
        self.gender = str()
        self.photo_url = True
        self.created_at = None
        self.updated_at = None
       
    @staticmethod 
    def abstract_table():
        pass
    
    def __str__(self):
        return (f"id: {self.id} Name: {self.first_name} {self.last_name}")

if __name__ == "__main__":
    result = Users().get({"email": "abc@test.com"})
    print(result)