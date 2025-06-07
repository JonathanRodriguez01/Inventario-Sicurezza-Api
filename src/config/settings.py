"""
Configuración de la aplicación a partir de variables de entorno.

Este módulo define la clase Settings, que permite centralizar y gestionar
las configuraciones leídas desde un archivo .env mediante Pydantic Settings.
"""

# Importación de terceros
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuración centralizada que carga parámetros desde variables de entorno.

    Atributos:
        productos_path (str): Ruta al archivo JSON de productos.
        ventas_path (str): Ruta al archivo JSON de ventas.
        host (str): Dirección host para ejecutar el servidor.
        port (int): Puerto para ejecutar el servidor.
    """
    productos_path: str
    ventas_path: str
    host: str = "127.0.0.1"
    port: int = 8000

    class Config:
        """
        Configuración de Pydantic Settings para cargar desde archivo .env.
        """
        env_file = ".env"
        env_file_encoding = "utf-8"  # Recomendado por Pydantic


# Instancia única de configuración accesible globalmente
settings = Settings()
