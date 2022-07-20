from fastapi import APIRouter
from .models import Product, format_product

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "Inventory"}


@router.get('/products')
def get_products():
    return [format_product(pk) for pk in Product.all_pks()]


@router.get('/products/{product_id}')
def get_products(product_id: str):
    return format_product(Product.get(product_id).pk)


@router.post('/products', status_code=201)
def create_product(product: Product):
    return product.save()


@router.delete('/products/{product_id}')
def delete_product(product_id: str):
    return Product.delete(product_id)
