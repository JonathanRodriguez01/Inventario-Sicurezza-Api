"""
Controlador para la lógica de negocio de productos.
"""

from src.services.producto_service import ProductoService
from src.schemas.producto_schema import ProductoCreate, ProductoUpdate


class ProductoController:
    """
    Controlador que maneja la lógica entre los endpoints y el servicio.
    """

    def __init__(self, service: ProductoService):
        self.service = service

    async def listar_productos(self):
        """
        Lista todos los productos.
        """
        return self.service.listar_productos()

    async def obtener_producto(self, producto_id: int):
        """
        Retorna un producto por ID.
        """
        return self.service.obtener_producto(producto_id)

    async def crear_producto(self, data: ProductoCreate):
        """
        Crea un nuevo producto.
        """
        return self.service.crear_producto(data.dict())

    async def actualizar_producto(self, producto_id: int, data: ProductoUpdate):
        """
        Actualiza los datos de un producto.
        """
        return self.service.actualizar_producto(producto_id, data.dict(exclude_unset=True))

    async def eliminar_producto(self, producto_id: int):
        """
        Elimina un producto por ID.
        """
        return self.service.eliminar_producto(producto_id)

    async def ajustar_stock(self, producto_id: int, cantidad: int):
        """
        Ajusta el stock del producto.
        """
        return self.service.ajustar_stock(producto_id, cantidad)

    async def registrar_venta(self, producto_id: int):
        """
        Registra una venta del producto.
        """
        return self.service.registrar_venta(producto_id)
