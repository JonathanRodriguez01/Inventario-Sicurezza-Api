"""
Servicio que gestiona la lógica de negocio para inventario.
"""

from typing import List
from src.models.producto import Producto
from src.repositories.producto_repository import ProductoRepository


class InventarioService:
    """
    Lógica para operaciones de inventario basadas en productos.
    """

    def __init__(self):
        """
        Inicializa con un repositorio de productos.
        """
        self.repo = ProductoRepository()

    def obtener_stock_total(self) -> int:
        """
        Suma el stock de todos los productos.
        """
        productos = self.repo.obtener_productos()
        return sum(p.stock for p in productos)

    def listar_productos_bajo_stock(self, umbral: int = 5) -> List[Producto]:
        """
        Devuelve productos con stock menor o igual al umbral.
        """
        productos = self.repo.obtener_productos()
        return [p for p in productos if p.stock <= umbral]
