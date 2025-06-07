"""
Modelo Pydantic para representar un producto en el inventario.
"""

from pydantic import BaseModel, Field


class Producto(BaseModel):
    """
    Define la estructura y validaciones para un producto.

    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre descriptivo del producto.
        precio_costo (float): Costo unitario de adquisición.
        precio_venta (float): Precio unitario de venta.
        stock (int): Cantidad disponible en inventario.
    """

    id: int = Field(..., example=1)
    nombre: str = Field(..., example="Camiseta")
    precio_costo: float = Field(..., gt=0, example=10.5)
    precio_venta: float = Field(..., gt=0, example=20.0)
    stock: int = Field(..., ge=0, example=100)
