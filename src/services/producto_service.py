"""
Módulo de servicio para la gestión de productos.

Define la lógica de negocio relacionada con los productos, sirviendo de intermediario
entre el controlador y el repositorio.
"""

from typing import List, Optional
from src.models.producto import Producto


class ProductoService:
    """
    Servicio que maneja la lógica de negocio para productos.
    """

    def __init__(self, productos: Optional[List[Producto]] = None):
        """
        Inicializa el servicio con una lista de productos.

        Args:
            productos (Optional[List[Producto]]): Lista inicial de productos.
                Si no se provee, se inicializa como lista vacía.
        """
        if productos is None:
            productos = []
        self.productos = productos

    def listar_productos(self, nombre: Optional[str] = None) -> List[Producto]:
        """
        Lista productos, opcionalmente filtrando por nombre parcial.

        Args:
            nombre (Optional[str]): Nombre parcial para filtrar productos.

        Returns:
            List[Producto]: Lista de productos filtrados o todos si no hay filtro.
        """
        if nombre is None:
            return self.productos
        return [
            producto for producto in self.productos
            if nombre.lower() in producto.nombre.lower()
        ]

    def obtener_producto_por_id(self, producto_id: int) -> Optional[Producto]:
        """
        Obtiene un producto por su ID.

        Args:
            producto_id (int): ID del producto a obtener.

        Returns:
            Optional[Producto]: Producto encontrado o None si no existe.
        """
        for producto in self.productos:
            if producto.id == producto_id:
                return producto
        return None

    def crear_producto(self, nuevo_producto: Producto) -> Producto:
        """
        Crea un nuevo producto y lo añade a la lista.

        Args:
            nuevo_producto (Producto): Producto a crear.

        Returns:
            Producto: Producto creado.
        """
        self.productos.append(nuevo_producto)
        return nuevo_producto

    def actualizar_producto(self, producto_id: int,
                            datos_actualizados: dict) -> Optional[Producto]:
        """
        Actualiza un producto existente con los datos proporcionados.

        Args:
            producto_id (int): ID del producto a actualizar.
            datos_actualizados (dict): Datos para actualizar el producto.

        Returns:
            Optional[Producto]: Producto actualizado o None si no existe.
        """
        producto = self.obtener_producto_por_id(producto_id)
        if not producto:
            return None

        for campo, valor in datos_actualizados.items():
            if hasattr(producto, campo):
                setattr(producto, campo, valor)
        return producto

    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Elimina un producto por su ID.

        Args:
            producto_id (int): ID del producto a eliminar.

        Returns:
            bool: True si se eliminó el producto, False si no se encontró.
        """
        for i, producto in enumerate(self.productos):
            if producto.id == producto_id:
                del self.productos[i]
                return True
        return False
