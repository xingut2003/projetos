from typing import List, Optional
from app.models.product import Product
from store.core.errors.exceptions import NotFoundError
from bson import ObjectId

def create_product(product_data: dict) -> Product:
    new_product = Product(**product_data).save()
    return new_product

def get_product(product_id: str) -> Product:
    product = Product.objects(id=ObjectId(product_id)).first()
    if not product:
        raise NotFoundError(f"Product with id {product_id} not found")
    return product
def get_all_products() -> List[Product]:
    return list(Product.objects().all())

def update_product(product_id: str, product_data: dict) -> Product:
    updated_product = Product.objects(id=ObjectId(product_id)).update_one(**product_data)
    if updated_product.modified_count == 0:
        raise NotFoundError(f"Product with id {product_id} not found")
    return Product.objects(id=ObjectId(product_id)).first()

def delete_product(product_id: str) -> None:
    deleted_product = Product.objects(id=ObjectId(product_id)).delete()
    if deleted_product == 0:
        raise NotFoundError(f"Product with id {product_id} not found")