import pytest
from pydantic import ValidationError

from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    """
    Este teste verifica se o modelo `ProductIn` do Schema valida com sucesso
    dados completos.

    Cenário: Cria dados de produto válidos utilizando o factory `product_data`.
            Valida esses dados utilizando o método `model_validate` do modelo
            `ProductIn`.

    Espere:
        * Validação bem-sucedida e criação de uma instância do modelo
        `ProductIn`.
        * Verifica o valor de um campo específico para demonstrar a posse dos
        dados.
    """
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"


def test_schemas_return_raise():
    """
    Este teste verifica se o modelo `ProductIn` do Schema levanta uma exceção 
    `ValidationError` quando faltam dados obrigatórios.

    Cenário: Cria dados de produto parcialmente preenchidos (faltando o campo
    'status').
            Tenta validar esses dados utilizando o método `model_validate` do
            modelo `ProductIn`
            envolvendo o código em um bloco `with pytest.raises` para capturar
            a exceção.

    Espere:
        * Levantamento da exceção `ValidationError`.
        * Verifica o conteúdo do erro para garantir que o campo 'status' está
        faltando.
    """
    data = {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
