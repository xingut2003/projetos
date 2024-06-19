import pytest
from pymongo import errors
from pydantic import UniqueKeyError, NotFoundError
from store.core.use_cases.product import (
    create_product, get_product, get_all_products,
    update_product, delete_product
)
from tests.factories import product_data

@pytest.fixture(scope="module")
def mongodb_client():
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://davitrabalhos2024:pRpTRCCgH0zzefrF@projeto1.crwhktw.mongodb.net/projeto")
    yield client
    client.close()

# Testes para create_product
def test_create_product(mongodb_client):
    product = product_data()
    created_product = create_product(product)
    assert created_product.name == product["name"]
    assert created_product.price == product["price"]

def test_create_product_duplicate_name(mongodb_client):
    product = product_data()
    create_product(product)  # Cria um produto
    with pytest.raises(UniqueKeyError):
        create_product(product)  # Tenta criar outro com o mesmo nome

# Testes para get_product
def test_get_product(mongodb_client):
    product = product_data()
    created_product = create_product(product)
    retrieved_product = get_product(str(created_product.id))
    assert retrieved_product.id == created_product.id

def test_get_product_not_found(mongodb_client):
    with pytest.raises(NotFoundError):
        get_product("inexistent_id")

# Testes para get_all_products
def test_get_all_products(mongodb_client):
    products = [product_data() for _ in range(3)]
    for product in products:
        create_product(product)
    all_products = get_all_products()
    assert len(all_products) >= 3

# Testes para update_product
def test_update_product(mongodb_client):
    product = product_data()
    created_product = create_product(product)
    updated_data = {"name": "Produto Atualizado", "price": 5000.00}
    updated_product = update_product(str(created_product.id), updated_data)
    assert updated_product.name == "Produto Atualizado"
    assert updated_product.price == 5000.00

def test_update_product_not_found(mongodb_client):
    with pytest.raises(NotFoundError):
        update_product("inexistent_id", product_data())

# Testes para delete_product
def test_delete_product(mongodb_client):
    product = product_data()
    created_product = create_product(product)
    delete_product(str(created_product.id))
    with pytest.raises(NotFoundError):
        get_product(str(created_product.id))

def test_delete_product_not_found(mongodb_client):
    with pytest.raises(NotFoundError):
        delete_product("inexistent_id")