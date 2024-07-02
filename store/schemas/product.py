from decimal import Decimal
from typing import Annotated, Optional

from bson import Decimal128
from pydantic import AfterValidator, Field

from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseSchemaMixin):
    """
    Classe base para Schemas de produto, contendo campos comuns.

    Esta classe base define os campos comuns utilizados em outros Schemas
    relacionados a produtos.
    Ela herda da classe `BaseSchemaMixin` para obter o comportamento padrão.
    """
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    """
    Classe Schema para entrada de dados de produto.

    Esta classe herda de `ProductBase` e `BaseSchemaMixin`, representando o
    schema de entrada de dados para produtos. Provavelmente utilizada em
    requisições para criar novos produtos.
    """
    ...


class ProductOut(ProductIn, OutSchema):
    """
    Classe Schema para saída de dados de produto.

    Esta classe herda de `ProductIn` e `OutSchema`, representando o schema de
    saída de dados para produtos. Provavelmente utilizada em respostas de
    consultas de produtos.
    Ela inclui os campos do produto (`ProductIn`) e adiciona os campos
    padronizados de saída definidos em `OutSchema` (id, created_at,
    updated_at).
    """
    ...


def convert_decimal_128(v):
    """
    Converte um valor decimal do Python para um valor Decimal128 do MongoDB.

    Esta função é utilizada como um validador posterior (`AfterValidator`)
    para garantir que os valores decimais armazenados no campo `price` da
    classe `ProductUpdate` sejam convertidos para o formato apropriado 
    utilizado pelo MongoDB (Decimal128) antes da serialização do Schema.

    Parâmetros:
        v (Decimal): O valor decimal do Python a ser convertido.

    Retorno:
        Decimal128: O valor convertido para Decimal128 do MongoDB.
    """
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    """
    Classe Schema para atualização parcial de dados de produto.

    Esta classe permite a atualização parcial de dados de um produto existente.
    Ela herda de `BaseSchemaMixin` e define campos opcionais para quantidade,
    preço e status.
    """
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    """
    Classe Schema para saída de dados de produto após atualização.

    Esta classe herda de `ProductOut`, provavelmente utilizada em respostas de
    requisições para atualização de produtos. Ela fornece o Schema completo do
    produto após a atualização.
    """
    ...
