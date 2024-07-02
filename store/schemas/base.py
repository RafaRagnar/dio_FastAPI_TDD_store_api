from datetime import datetime
from decimal import Decimal

from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
    """
    Classe Mixin para Schemas da aplicação.

    Esta classe mixin é herdada por outros Schemas para fornecer comportamento
    padrão.
    """
    class Config:
        from_attributes = True


class OutSchema(BaseModel):
    """
    Classe base para Schemas de saída de dados.

    Esta classe base é herdada por outros Schemas para representar dados de
    saída da aplicação.
    Ela herda da classe `BaseSchemaMixin` para obter o comportamento padrão e
    da classe `BaseModel` da biblioteca `pydantic` para funcionalidades de
    validação e serialização de dados.
    """
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator(mode="before")
    def set_schema(cls, data):
        """
        Validador de saída, converte Decimal128 do MongoDB para Decimal do
        Python.

        Este método validador é executado antes da serialização do Schema
        utilizando o decorador `@model_validator(mode="before")`. O método
        itera sobre os pares chave-valor do dicionário de dados (`data`) e
        verifica se o valor é do tipo `Decimal128` utilizado pelo MongoDB.
        Se for, o valor é convertido para o tipo `Decimal` do Python utilizando
        `Decimal(str(value))`.

        Args:
            cls (type): Classe do Schema (utilizado pelo decorador).
            data (dict): Dicionário contendo os dados a serem validados.

        Returns:
            dict: Dicionário contendo os dados validados e convertidos.
        """
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data
