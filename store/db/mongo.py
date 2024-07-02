from motor.motor_asyncio import AsyncIOMotorClient

from store.core.config import settings


class MongoClient:
    """
    Classe para gerenciar a conexão com o banco de dados MongoDB.

    Esta classe utiliza o driver assíncrono `motor.motor_asyncio` para
    estabelecer 
    uma conexão com o banco de dados e fornece acesso ao cliente do MongoDB.
    """
    def __init__(self) -> None:
        """
        Inicializa a instância da classe `MongoClient`.

        Estabelece a conexão com o banco de dados MongoDB utilizando a URL de
        conexão 
        definida na configuração da aplicação (`settings.DATABASE_URL`).
        """
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.DATABASE_URL
            )

    def get(self) -> AsyncIOMotorClient:
        """
        Retorna o cliente do banco de dados MongoDB.

        Este método fornece acesso ao cliente do MongoDB (`self.client`), 
        permitindo a interação com o banco de dados em outras partes da
        aplicação.
        """
        return self.client


db_client = MongoClient()
