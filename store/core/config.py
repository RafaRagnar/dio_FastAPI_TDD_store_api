from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Classe de configurações para a aplicação.

    Herda da classe `BaseSettings` da biblioteca `pydantic_settings`, 
    que fornece funcionalidades como carregamento automático de variáveis de
    ambiente e validação de dados.
    """
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
