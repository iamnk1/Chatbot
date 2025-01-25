from langgraph import LangGraph, Node, TextProcessor
from app.database.db import get_connection 

class ProductQueryAgent(LangGraph):
    def __init__(self):
        super().__init__()
        self.add_node(self.extract_query)
        self.add_node(self.get_product_details)

    def extract_query(self, text: str):
        """Extract the type of product query"""
        # Add logic to parse the query, e.g., extract product name
        if "product" in text.lower():
            return "fetch_product_details"

    def get_product_details(self, query_type):
        """Fetch product details from the database"""
        if query_type == "fetch_product_details":
            # Query the database and return product details
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Products;")
            products = cursor.fetchall()
            connection.close()
            return products
