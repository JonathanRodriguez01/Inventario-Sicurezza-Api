"""
Configuración de la aplicación a partir de variables de entorno.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuración centralizada que carga parámetros de entorno.

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
        Configuración interna de Pydantic Settings para especificar archivo de variables de entorno.
        """
        env_file = ".env"


settings = Settings()
