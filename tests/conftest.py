import asyncio
from uuid import UUID

import pytest
from httpx import AsyncClient

from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data


@pytest.fixture(scope="session")
def event_loop():
    """
    Este fixture configura um loop de eventos do asyncio para uso em testes
    assíncronos.

    O escopo `session` garante que o loop seja criado apenas uma vez por sessão
    de teste.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    """
    Este fixture retorna uma instância do cliente MongoDB obtida do módulo
    `db_client`.
    """
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    """
    Este fixture é executado automaticamente antes e depois de cada teste.

    Ele limpa todas as coleções do banco de dados MongoDB (exceto coleções do
    sistema).
    """
    yield
    collection_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:
    """
    Este fixture cria um cliente HTTP assíncrono para interagir com a API
    durante os testes.

    Ele utiliza o aplicativo (`app`) definido em `store.main` e configura a URL
    base como "http://test".
    """
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    """
    Este fixture define a URL base para os endpoints de produtos na API.
    """
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    """
    Este fixture fornece um ID de produto fixo em formato UUID.
    """
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id):
    """
    Este fixture cria uma instância do modelo `ProductIn` utilizando dados de
    fábrica (`product_data`).

    Ele também adiciona o `product_id` fornecido como argumento.
    """
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id):
    """
    Este fixture cria uma instância do modelo `ProductUpdate` utilizando dados
    de fábrica (`product_data`).

    Ele também adiciona o `product_id` fornecido como argumento.
    """
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in):
    """
    Este fixture cria um produto no banco de dados utilizando o caso de uso
    `product_usecase.create`.

    Ele recebe uma instância `product_in` e a utiliza para criar o produto.
    """
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in():
    """
    Este fixture cria uma lista de instâncias do modelo `ProductIn` utilizando
    dados de fábrica (`products_data`).
    """
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in):
    """
    Este fixture cria uma lista de produtos no banco de dados utilizando o caso
    de uso `product_usecase.create`.

    Ele recebe uma lista `products_in` e itera sobre ela, criando cada produto
    no banco.
    """
    return [await product_usecase.create(
        body=product_in) for product_in in products_in]
