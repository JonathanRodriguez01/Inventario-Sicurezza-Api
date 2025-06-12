"""
Controlador de inventario. Contiene lógica para operaciones relacionadas con el stock
de productos como listar productos con bajo stock o productos agotados.
"""

from typing import List
from src.models.producto import Producto
from src.services.producto_service import ProductoService


class InventarioController:
    """
    Controlador para operaciones relacionadas con el inventario de productos.
    """

    def __init__(self) -> None:
        """
        Inicializa el controlador con el servicio de productos.
        """
        self.service = ProductoService()

    def listar_productos_stock_bajo(self, umbral: int) -> List[Producto]:
        """
        Retorna los productos cuyo stock es menor o igual al umbral proporcionado.

        Args:
            umbral (int): Límite máximo de stock permitido.

        Returns:
            List[Producto]: Lista de productos con stock bajo.
        """
        return [p for p in self.service.productos if p.stock <= umbral]

    def listar_productos_agotados(self) -> List[Producto]:
        """
        Retorna los productos cuyo stock es exactamente 0.

        Returns:
            List[Producto]: Lista de productos agotados.
        """
        return [p for p in self.service.productos if p.stock == 0]
