"""
Repositorio que gestiona la persistencia de productos en memoria.
"""

from typing import List, Optional
from src.models.producto import Producto


class ProductoRepository:
    """
    Repositorio que almacena y recupera productos.
    """

    def __init__(self):
        """
        Inicializa con lista vacía de productos.
        """
        self._productos: List[Producto] = []

    def obtener_productos(self) -> List[Producto]:
        """
        Devuelve todos los productos.
        """
        return self._productos

    def obtener_producto_por_id(self, producto_id: int) -> Optional[Producto]:
        """
        Busca un producto por su ID.
        """
        for p in self._productos:
            if p.id == producto_id:
                return p
        return None

    def guardar(self, producto: Producto) -> Producto:
        """
        Agrega un producto.
        """
        self._productos.append(producto)
        return producto

    def actualizar(self, producto_id: int, datos: dict) -> Optional[Producto]:
        """
        Actualiza el producto con los datos indicados.
        """
        prod = self.obtener_producto_por_id(producto_id)
        if not prod:
            return None
        for campo, valor in datos.items():
            if hasattr(prod, campo):
                setattr(prod, campo, valor)
        return prod

    def eliminar(self, producto_id: int) -> bool:
        """
        Elimina un producto por ID.
        """
        for i, p in enumerate(self._productos):
            if p.id == producto_id:
                del self._productos[i]
                return True
        return False
