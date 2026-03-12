"""
Configurações da aplicação GNUVet.

Este arquivo centraliza todas as variáveis de ambiente
usadas pelo sistema.

Utiliza Pydantic Settings para carregar variáveis
do arquivo .env automaticamente.
"""

from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    # =============================
    # APPLICATION
    # =============================

    app_name: str = "GNUVet API"
    app_version: str = "1.0.0"

    # =============================
    # DATABASE
    # =============================

    database_url: str = "postgresql://gnuvet:gnuvet@localhost:5433/gnuvet"

    # =============================
    # SECURITY
    # =============================

    secret_key: str = "super-secret-key"
    algorithm: str = "HS256"

    # =============================
    # PYDANTIC CONFIG
    # =============================

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


# instância global das configurações
settings = Settings()