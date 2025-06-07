"""
Modelo Pydantic para representar una venta realizada.
"""

from pydantic import BaseModel, Field


class Venta(BaseModel):
    """
    Define la estructura y validaciones para una venta.

    Atributos:
        id (int): Identificador único de la venta.
        producto_id (int): ID del producto vendido.
        cantidad (int): Cantidad vendida.
        total (float): Total recaudado por la venta.
    """

    id: int = Field(..., example=1)
    producto_id: int = Field(..., example=1)
    cantidad: int = Field(..., gt=0, example=5)
    total: float = Field(..., gt=0, example=100.0)
