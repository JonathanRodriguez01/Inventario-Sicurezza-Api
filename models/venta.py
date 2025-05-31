"""
Modelo de datos para registrar ventas.
"""

from pydantic import BaseModel, Field

class Venta(BaseModel):
    producto_id: int = Field(..., description="ID del producto vendido")
    cantidad_vendida: int = Field(..., gt=0, description="Cantidad vendida del producto")
