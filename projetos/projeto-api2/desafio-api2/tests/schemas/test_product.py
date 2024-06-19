from uuid import UUID

from pymongo import errors
from pydantic import ValidationError
from typing import Dict

import pytest
from store.core.errors.exceptions import NotFoundError, UniqueKeyError
from store.core.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(product_data())

    assert product.name == "Readmi 15"
    assert isinstance(product.id, UUID)

def test_schemas_return_raise():
    data = {'name': "Readmi 15", 'quantity': 10, 'price': 4.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)


    assert err.value.errors()[0] == {'type': 'missing', 'loc': ('status',), 'msg': 'Field required', 'input': {'name': 'Readmi 15', 'quantity': 10, 'price': 4.5}, 'url': 'https://errors.pydantic.dev/2.7/v/missing'}

def create_product(product: Dict) -> ProductIn:
    try:
        new_product = ProductIn(**product).save()
        return new_product
    except errors.DuplicateKeyError:
        raise UniqueKeyError("Produto já existe.")

def update_product(product_id: str, product: Dict) -> ProductIn:
    updated_product = ProductIn.objects(id=product_id).update_one(**product)
    if updated_product.modified_count == 0:
        raise NotFoundError(f"Product with id {product_id} not found")
    return ProductIn.objects(id=product_id).first()