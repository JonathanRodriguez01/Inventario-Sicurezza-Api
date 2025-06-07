"""
Modelo de datos para la entidad Inventario.

Define la estructura del inventario en memoria, utilizada por los repositorios.
"""

from dataclasses import dataclass


@dataclass
class Inventario:
    """
    Representa un registro de inventario asociado a un producto.

    Atributos:
        id (int): Identificador único del inventario.
        producto_id (int): ID del producto al que pertenece el inventario.
        cantidad (int): Cantidad disponible del producto en inventario.
    """
    id: int
    producto_id: int
    cantidad: int
