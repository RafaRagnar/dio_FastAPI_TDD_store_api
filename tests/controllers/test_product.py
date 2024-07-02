from typing import List

import pytest
from fastapi import status

from tests.factories import product_data


async def test_controller_create_should_return_success(client, products_url):
    """
    Este teste verifica se o endpoint POST para criação de produtos retorna o
    status HTTP 201 Created e os dados do produto criado.

    Cenário: Realiza uma requisição POST para a URL de produtos com dados
    válidos.

    Espere:
        * Status code HTTP 201 Created.
        * Corpo da resposta contendo os dados do produto criado (sem campos
        automáticos).
    """
    response = await client.post(products_url, json=product_data())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    """
    Este teste verifica se o endpoint GET para obtenção de um produto
    específico retorna o status HTTP 200 OK e os dados do produto.

    Cenário: Realiza uma requisição GET para a URL de um produto específico
    (já inserido).

    Espere:
        * Status code HTTP 200 OK.
        * Corpo da resposta contendo os dados do produto (sem campos
        automáticos).
    """
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    """
    Este teste verifica se o endpoint GET para obtenção de um produto
    inexistente retorna o status HTTP 404 Not Found.

    Cenário: Realiza uma requisição GET para a URL de um produto com ID
    inexistente.

    Espere:
        * Status code HTTP 404 Not Found.
        * Corpo da resposta contendo a mensagem de erro.
    """
    response = await client.get(
        f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
        }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, products_url):
    """
    Este teste verifica se o endpoint GET para listagem de produtos retorna o
    status HTTP 200 OK e uma lista de produtos.

    Cenário: Realiza uma requisição GET para a URL de listagem de produtos
    (com fixture para inserir produtos).

    Espere:
        * Status code HTTP 200 OK.
        * Corpo da resposta contendo uma lista de produtos (formato de lista
        verificado).
    """
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    """
    Este teste verifica se o endpoint PATCH para atualização parcial de um
    produto retorna o status HTTP 200 OK e os dados do produto atualizado.

    Cenário: Realiza uma requisição PATCH para a URL de um produto específico, 
    atualizando apenas o campo 'price'.

    Espere:
        * Status code HTTP 200 OK.
        * Corpo da resposta contendo os dados do produto atualizado (sem
        campos automáticos).
    """
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "7.500"}
    )

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "7.500",
        "status": True,
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    """
    Este teste verifica se o endpoint DELETE para exclusão de um produto
    retorna o status HTTP 204 No Content.

    Cenário: Realiza uma requisição DELETE para a URL de um produto específico
    (já inserido).

    Espere:
        * Status code HTTP 204 No Content (sem corpo de resposta).
    """
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    """
    Este teste verifica se o endpoint DELETE para exclusão de um produto
    inexistente retorna o status HTTP 404 Not Found.

    Cenário: Realiza uma requisição DELETE para a URL de um produto com ID
    inexistente.

    Espere:
        * Status code HTTP 404 Not Found.
        * Corpo da resposta contendo a mensagem de erro.
    """
    response = await client.delete(
        f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }
