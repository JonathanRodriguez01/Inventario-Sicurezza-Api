"""
Schemas Pydantic para la entidad Inventario.
"""

from typing import Optional
from pydantic import BaseModel


class InventarioBase(BaseModel):
    """
    Schema base para un registro de inventario.
    """
    producto_id: int
    cantidad: int


class InventarioCreate(InventarioBase):
    """
    Schema para crear un registro de inventario.
    """
    # Hereda todos los campos de InventarioBase; no se añaden nuevos campos.


class InventarioUpdate(BaseModel):
    """
    Schema para actualizar un registro de inventario.
    Todos los campos son opcionales.
    """
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None


class InventarioResponse(InventarioBase):
    """
    Schema para la respuesta del inventario.
    Incluye el ID del registro.
    """
    id: int

    class Config:
        """
        Configuración para permitir compatibilidad con ORMs.
        """
        orm_mode = True
