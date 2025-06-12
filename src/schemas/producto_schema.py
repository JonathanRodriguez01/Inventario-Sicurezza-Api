"""
Schemas Pydantic para la entidad Producto. Se utilizan para validación y serialización
de datos en las operaciones de entrada y salida de la API.
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductoBase(BaseModel):
    """
    Campos comunes para un producto.

    Atributos:
        nombre (str): Nombre del producto.
        descripcion (str): Descripción del producto.
        precio (float): Precio unitario.
        cantidad (int): Stock disponible.
    """
    nombre: str
    descripcion: str
    precio: float
    cantidad: int


class ProductoCreate(ProductoBase):
    """
    Esquema para crear un producto.
    Hereda todos los campos del esquema base.
    """


class ProductoUpdate(BaseModel):
    """
    Esquema para actualizar un producto.

    Atributos opcionales para permitir actualizaciones parciales.
    """
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    cantidad: Optional[int] = None


class ProductoResponse(ProductoBase):
    """
    Esquema de respuesta para un producto.

    Atributos:
        id (int): Identificador único.
    """
    id: int
    model_config = ConfigDict(from_attributes=True)
