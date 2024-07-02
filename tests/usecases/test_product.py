from typing import List
from uuid import UUID

import pytest

from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_in):
    """
    Este teste verifica se o caso de uso `product_usecase.create` cria um
    produto e retorna a sua representação de saída (`ProductOut`).

    Cenário: Realiza uma chamada ao caso de uso `create` passando dados válidos 
            como entrada (`product_in`).

    Espere:
        * Retorno de uma instância do modelo `ProductOut`.
        * Verifica o valor de um campo específico para demonstrar a criação do
        produto.
    """
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    """
    Este teste verifica se o caso de uso `product_usecase.get` retorna um
    produto pelo seu identificador (`id`).

    Cenário: Recupera o identificador de um produto previamente inserido
    (`product_inserted`).
            Realiza uma chamada ao caso de uso `get` passando o identificador
            como argumento.

    Espere:
        * Retorno de uma instância do modelo `ProductOut`.
        * Verifica o valor de um campo específico para demonstrar a busca
        bem-sucedida.
    """
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    """
    Este teste verifica se o caso de uso `product_usecase.get` levanta a
    exceção `NotFoundException` quando o produto não é encontrado.

    Cenário: Tenta buscar um produto utilizando um identificador inexistente.
            Envolve o código de busca em um bloco `with pytest.raises` para
            capturar a exceção.

    Espere:
        * Levantamento da exceção `NotFoundException`.
        * Verifica a mensagem de erro para garantir que o identificador
            informado está correto.
    """
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID(
            "1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    """
    Este teste verifica se o caso de uso `product_usecase.query` retorna uma
    lista de produtos.

    Cenário: Realiza uma chamada ao caso de uso `query` para listar produtos 
            (com fixture para inserir produtos).

    Espere:
        * Retorno de uma lista de produtos.
        * Verifica o tamanho da lista para garantir que há produtos.
    """
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_up,
                                                     product_inserted):
    """
    Este teste verifica se o caso de uso `product_usecase.update` atualiza um
    produto e retorna a sua representação de saída (`ProductUpdateOut`).

    Cenário: Recupera o identificador de um produto previamente inserido
    (`product_inserted`).
            Cria dados de atualização (`atualizacao_produto`) modificando o
            preço.
            Realiza uma chamada ao caso de uso `update` passando o
            identificador e os dados de atualização.

    Espere:
        * Retorno de uma instância do modelo `ProductUpdateOut`.
    """
    product_up.price = "7.500"
    result = await product_usecase.update(
        id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    """
    Este teste verifica se o caso de uso `product_usecase.delete` exclui um
    produto e retorna `True`.

    Cenário: Recupera o identificador de um produto previamente inserido
    (`product_inserted`).
            Realiza uma chamada ao caso de uso `delete` passando o
            identificador.

    Espere:
        * Retorno de `True` indicando a exclusão bem-sucedida.
    """
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    """
    Este teste verifica se o caso de uso `product_usecase.delete` levanta a
    exceção `NotFoundException` quando o produto não é encontrado.

    Cenário: Tenta excluir um produto utilizando um identificador inexistente.
            Envolve o código de exclusão em um bloco `with pytest.raises` para
            capturar a exceção.

    Espere:
        * Levantamento da exceção `NotFoundException`.
        * Verifica a mensagem de erro para garantir que o identificador
            informado está correto.
    """
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID(
            "1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
