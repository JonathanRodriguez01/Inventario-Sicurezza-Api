"""
Módulo controlador para la gestión de productos.

Define la clase ProductoController que maneja la lógica de negocio relacionada
con los productos, sirviendo de intermediario entre las rutas y los servicios.
"""

from typing import List, Optional

from src.services.producto_service import ProductoService
from src.schemas.producto_schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse
)


class ProductoController:
    """
    Controlador que maneja la lógica de las operaciones sobre productos.
    Recibe peticiones desde las rutas y llama al servicio correspondiente.
    """

    def __init__(self, service: ProductoService):
        """
        Inicializa el controlador con una instancia del servicio de productos.

        Args:
            service (ProductoService): Servicio que maneja la lógica de negocio.
        """
        self.service = service

    def listar_productos(self, nombre: Optional[str] = None) -> List[ProductoResponse]:
        """
        Lista productos, opcionalmente filtrando por nombre parcial.

        Args:
            nombre (Optional[str]): Nombre parcial para filtrar productos.

        Returns:
            List[ProductoResponse]: Lista de productos filtrados o todos si no hay filtro.
        """
        productos = self.service.listar_productos(nombre)
        return [ProductoResponse.from_orm(prod) for prod in productos]

    def obtener_producto(self, producto_id: int) -> ProductoResponse:
        """
        Obtiene un producto por su ID.

        Args:
            producto_id (int): ID del producto a obtener.

        Returns:
            ProductoResponse: Producto encontrado.

        Raises:
            HTTPException: Si el producto no existe.
        """
        producto = self.service.obtener_producto_por_id(producto_id)
        return ProductoResponse.from_orm(producto)

    def crear_producto(self, producto_data: ProductoCreate) -> ProductoResponse:
        """
        Crea un nuevo producto.

        Args:
            producto_data (ProductoCreate): Datos del producto a crear.

        Returns:
            ProductoResponse: Producto creado.
        """
        nuevo_producto = self.service.crear_producto(producto_data)
        return ProductoResponse.from_orm(nuevo_producto)

    def actualizar_producto(
        self,
        producto_id: int,
        producto_data: ProductoUpdate
    ) -> ProductoResponse:
        """
        Actualiza un producto existente.

        Args:
            producto_id (int): ID del producto.
            producto_data (ProductoUpdate): Nuevos datos.

        Returns:
            ProductoResponse: Producto actualizado.
        """
        producto_actualizado = self.service.actualizar_producto(
            producto_id,
            producto_data
        )
        return ProductoResponse.from_orm(producto_actualizado)

    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Elimina un producto por su ID.

        Args:
            producto_id (int): ID del producto a eliminar.

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró.
        """
        return self.service.eliminar_producto(producto_id)
