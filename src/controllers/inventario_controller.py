"""
Controlador para la gestión del inventario.

Este módulo define la clase InventarioController, que actúa como intermediario entre
las rutas de inventario y el servicio correspondiente.
"""

from typing import List
from src.models.producto import Producto
from src.services.inventario_service import InventarioService


class InventarioController:
    """
    Controlador que maneja la lógica de las operaciones sobre el inventario.
    """

    def __init__(self, service: InventarioService):
        """
        Inicializa el controlador con una instancia del servicio de inventario.

        Args:
            service (InventarioService): Servicio que maneja la lógica de negocio del inventario.
        """
        self.service = service

    def calcular_precio_venta(self, costo: float, margen: float = 0.30) -> float:
        """
        Calcula el precio de venta de un producto.

        Args:
            costo (float): Costo base del producto.
            margen (float): Margen de ganancia deseado (por defecto 30%).

        Returns:
            float: Precio de venta sugerido.
        """
        return self.service.calcular_precio_venta(costo, margen)

    def obtener_stock_total(self) -> int:
        """
        Obtiene la cantidad total de unidades en stock.

        Returns:
            int: Total de unidades disponibles.
        """
        return self.service.obtener_stock_total()

    def obtener_productos_bajo_stock(self, umbral: int = 5) -> List[Producto]:
        """
        Obtiene una lista de productos cuyo stock es menor al umbral.

        Args:
            umbral (int): Umbral de stock bajo. Por defecto es 5.

        Returns:
            List[Producto]: Productos con stock bajo.
        """
        return self.service.listar_productos_bajo_stock(umbral)
