import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any

from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_serializer


class CreateBaseModel(BaseModel):
    """
    Classe base para modelos de criação de dados.

    Esta classe base fornece campos e funcionalidades comuns utilizados na
    criação de modelos para dados novos na aplicação. Ela herda da classe
    `BaseModel` da biblioteca `pydantic`.
    """

    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        """
        Serializa o modelo para um dicionário, convertendo valores decimais
        para Decimal128 do MongoDB.

        Este método utiliza o decorador `@model_serializer` da biblioteca
        `pydantic` para converter a instância do modelo em um dicionário.
        O método itera sobre os pares chave-valor do dicionário e verifica se
        o valor é do tipo `Decimal`. Se for, o valor é convertido para o tipo
        `Decimal128` utilizado pelo MongoDB para armazenar dados decimais com
        alta precisão.

        Returns:
            dict[str, Any]: Dicionário contendo os dados do modelo
            serializados.
        """
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

        return self_dict
