"""
Modelo de datos para productos del inventario.
"""

from pydantic import BaseModel, Field

class Producto(BaseModel):
    id: int = Field(default=None, description="ID único del producto")
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: str = Field(..., description="Descripción del producto")
    precio_costo: float = Field(..., gt=0, description="Precio de costo del producto")
    precio_venta: float = Field(..., gt=0, description="Precio de venta del producto")
    stock: int = Field(..., ge=0, description="Cantidad disponible en stock")
    unidades_vendidas: int = Field(0, ge=0, description="Unidades vendidas del producto")
