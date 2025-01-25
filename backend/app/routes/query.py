from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/query")
def query_products(text: str):
    connection = get_connection()
    if connection is None:
        return {"message": "Database connection error"}

    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM Products WHERE Brand LIKE '%{text}%';"
        cursor.execute(query)
        products = cursor.fetchall()

        if not products:
            return {"message": "No products found for the specified query."}

        product_list = []
        for product in products:
            product_data = {
                "ID": product[0],
                "Name": product[1],
                "Brand": product[2],
                "Price": product[3],
                "Category": product[4],
                "Description": product[5],
            }
            product_list.append(product_data)

        return {"products": product_list}

    except Exception as e:
        return {"message": str(e)}

    finally:
        connection.close()
