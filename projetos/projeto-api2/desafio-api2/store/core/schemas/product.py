from store.core.schemas.base import BaseSechemasMixin
from pydantic import Field


class ProductIn(BaseSechemasMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")