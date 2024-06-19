from fastapi import APIRouter, HTTPException, status
from store.core.errors.exceptions import NotFoundError, UniqueKeyError

router = APIRouter()

@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: str):
    try:
        product = get_product(product_id)
        return product
    except NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=e.message
        )