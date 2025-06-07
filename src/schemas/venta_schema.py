"""
Schemas Pydantic para la entidad Venta.
"""

from typing import Optional
from pydantic import BaseModel


class VentaBase(BaseModel):
    """
    Schema base para una venta.
    """
    producto_id: int
    cantidad: int
    total: float


class VentaCreate(VentaBase):
    """
    Schema para crear una venta.
    """
    # Hereda todos los campos de VentaBase; no se añaden nuevos campos.


class VentaUpdate(BaseModel):
    """
    Schema para actualizar una venta.
    Todos los campos son opcionales.
    """
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None
    total: Optional[float] = None


class VentaResponse(VentaBase):
    """
    Schema para la respuesta de una venta.
    Incluye el ID único de la venta.
    """
    id: int

    class Config:
        """
        Configuración para permitir la compatibilidad con ORMs.
        """
        orm_mode = True
