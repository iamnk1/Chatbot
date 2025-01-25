from fastapi import APIRouter, HTTPException
from app.database.db import get_connection 

router = APIRouter()

@router.get("/products")
def get_products():
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products;")
        products = cursor.fetchall()  # Get all rows from the Products table
        
        if not products:
            return {"message": "No products found"}
        
        # Create a structured response
        product_list = []
        for product in products:
            product_data = {
                "ID": product[0],
                "Name": product[1],
                "Brand": product[2],
                "Price": product[3],
                "Category": product[4],
                "Description": product[5],
                "SupplierID": product[6]
            }
            product_list.append(product_data)
        
        return {"products": product_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        connection.close()  # Close the connection after use
