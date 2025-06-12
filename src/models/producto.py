"""
Modelo de dominio para representar un producto.
"""

from pydantic import BaseModel


class Producto(BaseModel):
    """
    Modelo que representa un producto con sus atributos principales.
    
    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        stock (int): Cantidad disponible en inventario.
    """
    id: int
    nombre: str
    precio: float
    stock: int
