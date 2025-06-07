"""
Schemas Pydantic para la entidad Producto.
"""

from typing import Optional
from pydantic import BaseModel


class ProductoBase(BaseModel):
    """
    Schema base para un producto.
    """
    nombre: str
    descripcion: Optional[str] = None
    precio: float


class ProductoCreate(ProductoBase):
    """
    Schema para crear un producto.
    """
    # Hereda todos los campos de ProductoBase; no se añaden nuevos campos.


class ProductoUpdate(BaseModel):
    """
    Schema para actualizar un producto.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None


class ProductoResponse(ProductoBase):
    """
    Schema para la respuesta de un producto.
    Incluye el ID del producto.
    """
    id: int

    class Config:
        """
        Configuración para permitir compatibilidad con ORMs.
        """
        orm_mode = True
