"""
Módulo de repositorio para la gestión del inventario.

Este módulo administra el stock de productos almacenados, permitiendo
consultar, modificar y eliminar cantidades.
"""

from typing import Optional


class InventarioRepository:
    """
    Repositorio que gestiona el inventario de productos y sus cantidades.
    """

    def __init__(self):
        """
        Inicializa el inventario como un diccionario vacío donde
        la clave es el ID del producto y el valor es la cantidad en stock.
        """
        self._stock = {}

    def obtener_cantidad(self, producto_id: int) -> Optional[int]:
        """
        Obtiene la cantidad en stock de un producto dado su ID.

        Args:
            producto_id (int): ID del producto.

        Returns:
            Optional[int]: Cantidad disponible o None si no existe.
        """
        return self._stock.get(producto_id)

    def agregar_stock(self, producto_id: int, cantidad: int) -> None:
        """
        Agrega una cantidad al stock del producto.

        Args:
            producto_id (int): ID del producto.
            cantidad (int): Cantidad a agregar. Puede ser positiva o negativa.
        """
        actual = self._stock.get(producto_id, 0)
        self._stock[producto_id] = actual + cantidad

    def establecer_stock(self, producto_id: int, cantidad: int) -> None:
        """
        Establece la cantidad exacta de stock de un producto.

        Args:
            producto_id (int): ID del producto.
            cantidad (int): Cantidad exacta a establecer.
        """
        self._stock[producto_id] = cantidad

    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Elimina el producto del inventario.

        Args:
            producto_id (int): ID del producto a eliminar.

        Returns:
            bool: True si se eliminó, False si no existía.
        """
        if producto_id in self._stock:
            del self._stock[producto_id]
            return True
        return False
