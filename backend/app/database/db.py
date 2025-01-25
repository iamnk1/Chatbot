import mysql.connector
from mysql.connector import Error
import sqlite3 

def get_connection():
    connection = sqlite3.connect('your_database.db')
    return connection
   
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",       
            user="root",     
            password="Nanda@2001",
            database="product_supplier_db" 
        )
        if connection.is_connected():
            print("Database connection successful.")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
