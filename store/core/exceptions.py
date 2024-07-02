class BaseException(Exception):
    """
    Classe base para exceções personalizadas na aplicação.

    Herda da classe `Exception` embutida do Python e fornece funcionalidades 
    para lidar com erros de forma mais específica e organizada.
    """
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message


class NotFoundException(BaseException):
    """
    Exceção personalizada para indicar que um recurso não foi encontrado na
    aplicação.

    Herda da classe `BaseException` e representa um erro específico para casos 
    onde um recurso esperado, como um produto ou outro dado, não é encontrado.
    """
    message = "Not Found"
