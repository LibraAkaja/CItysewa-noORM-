import os
import datetime
from abc import ABC, abstractmethod

import django
from django.db import connection
from django.utils import timezone

from .schema import table_queries

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


class SchemaManager:
    def test_connection(self):
        test_query = "SELECT 1;"
        try:
            with connection.cursor() as cursor:
                cursor.execute(test_query)
                return True if cursor.fetchone()[0] else False
        except Exception as e:
            print(f"{e}")
            return False
    
    def migrate(self, table_name, query):
        if not self.test_connection():
            return "Error: Couldn`t connect to the database."
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
            return f"Table: {table_name} created successfully."
            
        except Exception as e:
            connection.rollback()
            return f"Error: Unable to create table. {e}"
    
    def drop_table(self, table_name):        
        if not self.test_connection():
            return "Error: Couldn`t connect to the database."
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
            connection.commit()
            return f"Table:{table_name} deleted successfully."
            
        except Exception as e:
            connection.rollback()
            return f"Error: Unable to delete table. {e}"


class Table(ABC):
    table_name = None
    required_fields = []    
    read_only_fields = ['id', 'created_at', 'updated_at']
    _attrs = {
        "id": int,
        "created_at": datetime.datetime,
        "updated_at": datetime.datetime
    }
    
    def __init__(self):
        pass
    
    @abstractmethod
    def abstract_method(self):
        '''This method is only mentioned to make this class abstract.'''
        pass
    
    def __setattr__(self, key, value):
        if not isinstance(value, self._attrs[key]):
            raise TypeError(f"{key} must be {self._attrs[key].__name__}")
        return super().__setattr__(key, value)
    
    def count(self):
        pass
    
    def all(self):
        query = f"SELECT * FROM {self.table_name}"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error: {e}")
            return
            
    def get(self, **kwargs):
        if len(kwargs) == 0:
            print("Atleast a field is required for searching rows.")
            return
        
        cols = [col for col in kwargs.keys() if col in self._attrs]
        values = tuple(kwargs[col] for col in cols)
        condition = " AND ".join([f'{col} = %s' for col in cols])
        query = f"SELECT * FROM {self.table_name} WHERE {condition};"
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                result = cursor.fetchone()
                if result:
                    res = list(result)
                    self.id, self.created_at, self.updated_at = res.pop(0), res.pop(-2), res.pop(-1)
                    keys = list(self._attrs.keys())
                    keys.remove("id")
                    for i,value in enumerate(res):
                        if value is not None:
                            self.__setattr__(keys[i], value)
                    return self
                return result
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def filter(self):
        pass
    
    def create(self, **kwargs):
        for key in self.required_fields:
            if key not in kwargs.keys():
                raise TypeError(f"Missing required field: {key}")
        
        for key, value in kwargs.items():
            if key in self._attrs.keys() and key not in self.read_only_fields:
                self.__setattr__(key, value)
                
        cols = ", ".join(list(self.__dict__.keys()))
        vals = tuple(self.__dict__.values())
        placeholders = ", ".join(['%s' for _ in vals])
        
        query = f"INSERT INTO {self.table_name} ({cols}) VALUES ({placeholders});"        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, vals)
            connection.commit()
            print(f"Record inserted successfully in the {self.table_name}.")
            return self
        except Exception as e:
            print(f"Error: {e}")
            return
        
    def update(self):
        current_time = timezone.now()
    
    def delete(self, **kwargs):
        if len(kwargs) == 0:
            print("Atleast a field is required for searching rows.")
            return
        
        cols = [col for col in kwargs.keys() if col in self._attrs]
        values = tuple(kwargs[col] for col in cols)
        condition = " AND ".join([f'{col} = %s' for col in cols])
        query = f"DELETE FROM {self.table_name} WHERE {condition};"
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                rows_deleted = cursor.rowcount
            connection.commit()
            print(f"{rows_deleted} records deleted from the {self.table_name}.")
        
        except Exception as e:
            print(f"Error: {e}")
        


if __name__ == "__main__":
    for table in table_queries: 
        print(SchemaManager().migrate(table_name=table, query=table_queries[table]))     
    
