"""
Configuración de variables de entorno para la aplicación.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Define las variables de entorno necesarias para la configuración de la app.

    Atributos:
        productos_path (str): Ruta al archivo JSON de productos.
        ventas_path (str): Ruta al archivo JSON de ventas.
        host (str): Dirección host para el servidor.
        port (int): Puerto para el servidor.
    """
    productos_path: str
    ventas_path: str
    host: str = "127.0.0.1"
    port: int = 8000

    class Config:
        """
        Configuración interna para indicar el archivo .env.
        """
        env_file = ".env"


settings = Settings()
