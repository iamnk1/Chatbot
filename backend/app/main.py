from fastapi import FastAPI
from app.routes.products import router as product_router
from app.routes.suppliers import router as supplier_router
from app.routes.query import router as query_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(query_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)