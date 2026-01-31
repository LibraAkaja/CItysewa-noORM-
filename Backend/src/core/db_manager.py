import datetime
from abc import ABC, abstractmethod

from django.db import connection

from .schema import table_queries

class SchemaManager:
    def test_connection(self):
        test_query = "SELECT 1;"
        try:
            with connection.cursor() as cursor:
                cursor.execute(test_query)
                if cursor.fetchone()[0]:
                    print("Database connection successful.")
                    return True
                print("Database connection failed.")
                return False
        except Exception as e:
            print("Database connection failed.")
            print(f"Error: {e}")
            return False
    
    def create_table(self, table_name, query):
        if not self.test_connection():
            print("Error: Couldn`t connect to the database.")
            return
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
            print(f"Table: {table_name} created successfully.")
            return
            
        except Exception as e:
            connection.rollback()
            print(f"Error: Unable to create table. {e}")
            return
    
    def drop_table(self, table_name):        
        if not self.test_connection():
            print("Error: Couldn`t connect to the database.")
            return
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
            connection.commit()
            print(f"Table:{table_name} deleted successfully.")
            return
            
        except Exception as e:
            connection.rollback()
            print(f"Error: Unable to delete table. {e}")
            return

# method for migrating tables to database
def migrate():
    manager = SchemaManager()
    for table_name in table_queries.keys():
        manager.create_table(table_name, table_queries[table_name])
        

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
        for key in self._attrs.keys():
            self.__setattr__(key, None)
    
    @abstractmethod
    def abstract_method(self):
        '''This method is only mentioned to make this class abstract.'''
        pass
    
    def __setattr__(self, key, value):
        if value and key in self._attrs and not isinstance(value, self._attrs[key]):
            raise TypeError(f"{key} must be {self._attrs[key].__name__}")
        return super().__setattr__(key, value)
           
    #C   
    def create(self, **kwargs):
        for key in self.required_fields:
            if key not in kwargs.keys():
                raise TypeError(f"Missing required field: {key}")
       
        for key, value in kwargs.items():
            if key in self._attrs and key not in self.read_only_fields:
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
            return self.get(**self.__dict__)
        except Exception as e:
            print(f"Error: {e}")
            return   
    
    #R         
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
                    columns = [col[0] for col in cursor.description]
                    obj = self.__class__()
                    for col,value in zip(columns, result):
                        if value is not None:
                            obj.__setattr__(col, value)
                    return obj
                return result
            
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    #R
    def filter(self):
        pass   
    
    #R
    def count(self, **kwargs):
        query = f"SELECT COUNT(*) FROM {self.table_name}"
        cols = [col for col in kwargs.keys() if col in self._attrs]
        values = ()
        if cols:
            condition = " AND ".join([f"{col} = %s" for col in cols])
            values = tuple([kwargs[col] for col in cols])
            query = f"{query} WHERE {condition}"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                total_rows = cursor.fetchone()[0]
                return total_rows
        except Exception as e:
            print(f"Error: {e}")
            return
    
    #R
    def all(self, order_by=None, order_type=0): # 0->ASC 1->DESC
        if order_by is not None and order_by not in self._attrs:
            raise ValueError("Invalid order_by field")
        order_type_list = ["ASC", "DESC"]
        query = f"SELECT * FROM {self.table_name}"
        if order_by:
            query = f"{query} ORDER BY {order_by} {order_type_list[order_type]}"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                cols = [col[0] for col in cursor.description]
                result = [dict(zip(cols, row)) for row in rows]                
                return result                
            
        except Exception as e:
            print(f"Error: {e}")
            return
    
    #R
    def join(self, right_table, join_on:tuple, left_attrs:tuple, right_attrs:tuple, left_conditions:dict={}, right_conditions:dict={}):
        if not all([isinstance(join_on, tuple), isinstance(left_attrs, tuple), isinstance(right_attrs, tuple), isinstance(left_conditions, dict), isinstance(right_conditions, dict)]):
            raise TypeError("Arguments type mismatch.")
        
        if not hasattr(self, join_on[0]):
            raise ValueError(f"{self.__class__.__name__} has no attribute {join_on[0]}.")
        if not hasattr(right_table, join_on[1]):
            raise ValueError(f"{right_table.__class__.__name__} has no attribute {join_on[1]}.")
        
        if not all(isinstance(item, str) for item in join_on):
            raise TypeError("join attributes must be string.")
        
        for left in left_attrs:
            if not hasattr(self, left):
                raise ValueError(f"{self.__class__.__name__} has no attribute {left}.")
        
        for right in right_attrs:  
            if not hasattr(right_table, right):
                raise ValueError(f"{right_table.__class__.__name__} has no attribute {right}.")
           
        for left_con in left_conditions:
            if not hasattr(self, left_con):
                raise ValueError(f"{self.__class__.__name__} has no attribute {left_con}.")
            
        for right_con in right_conditions:            
            if not hasattr(right_table, right_con):
                raise ValueError(f"{right_table.__class__.__name__} has no attribute {right_con}.")
            
        left_columns = ", ".join(f"X.{attr} as {self.table_name.rstrip("s")}_{attr}" for attr in left_attrs)
        right_columns = ", ".join(f"Y.{attr} as {right_table.table_name.rstrip("s")}_{attr}" for attr in right_attrs)
        query = f"SELECT {left_columns}, {right_columns} FROM {self.table_name} as X JOIN {right_table.table_name} as Y ON X.{join_on[0]} = Y.{join_on[1]}"
        
        values = ()
        if len(left_conditions)>0 or len(right_conditions)>0:
            where_clause_left = [f"X.{col} = %s" for col in left_conditions]
            values_left_con = tuple(left_conditions.values())
            
            where_clause_right = [f"Y.{col} = %s" for col in right_conditions]
            values_right_con = tuple(right_conditions.values())
            
            where_clause = " AND ".join([*where_clause_left, *where_clause_right])
            query = f"{query} WHERE {where_clause}"
            
            values = (*values_left_con, *values_right_con)
            
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                rows = cursor.fetchall()
                cols = [col[0] for col in cursor.description]
                result = [dict(zip(cols, row)) for row in rows]
                return result
        except Exception as e:
            print(f"Error: {e}")
            return

    #U  
    def update(self, **kwargs):
        if kwargs.get("id") is None:
            raise ValueError("Cannot update without ID")
        
        cols = [col for col in kwargs if col in self._attrs and col not in self.read_only_fields]
        values = [kwargs[col] for col in cols]
        
        set_clause = ", ".join(f"{col} = %s" for col in cols)
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s"
        
        values.append(kwargs["id"])
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
            connection.commit()
            print(f"Record updated successfully in the {self.table_name}.")
              
        except Exception as e:
            print(f"Error: {e}")
            
                
    #D
    def delete(self, **kwargs):
        cols = [col for col in kwargs.keys() if col in self._attrs]
        if len(cols) == 0:
            print("Atleast a field is required for searching rows.")
            return       
        
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
            
    def __str__(self):
        return (f"Table instance: {self.table_name}")

if __name__ == "__main__":
    migrate()   
