from fastapi import FastAPI

from store.core.config import settings
from store.routers import api_router


class App(FastAPI):
    """
    Classe personalizada do FastAPI para melhor organização e configuração.

    Esta classe herda do FastAPI e permite definir configurações personalizadas
    durante a inicialização, como versão, título e caminho raiz.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Inicializa a instância do App com configurações personalizadas.

        Args:
            *args: Argumentos posicional adicionais passados ao construtor do
            FastAPI.
            **kwargs: Argumentos de palavra-chave adicionais passados ao
            construtor do FastAPI.

        Returns:
            None
        """
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App()
app.include_router(api_router)
