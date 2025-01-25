from fastapi import APIRouter, HTTPException
from app.database.db import get_connection  # Import the database connection

router = APIRouter()

@router.get("/suppliers")
def get_suppliers():
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Suppliers;")
        suppliers = cursor.fetchall()  # Get all suppliers

        if not suppliers:
            return {"message": "No suppliers found"}

        supplier_list = []
        for supplier in suppliers:
            supplier_data = {
                "ID": supplier[0],
                "Name": supplier[1],
                "ContactInfo": supplier[2],
                "ProductCategories": supplier[3]
            }
            supplier_list.append(supplier_data)

        return {"suppliers": supplier_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        connection.close()  # Close the connection after use
