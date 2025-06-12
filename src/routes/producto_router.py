"""
Router para endpoints CRUD de productos.
"""

from typing import List
from fastapi import APIRouter, Body
from src.services.producto_service import ProductoService
from src.controllers.producto_controller import ProductoController
from src.schemas.producto_schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse
)

router = APIRouter()
service = ProductoService()
controller = ProductoController(service)


@router.get("/", response_model=List[ProductoResponse])
async def listar_productos():
    """
    Lista todos los productos.
    """
    return await controller.listar_productos()


@router.get("/{producto_id}", response_model=ProductoResponse)
async def obtener_producto(producto_id: int):
    """
    Retorna un producto por ID.
    """
    return await controller.obtener_producto(producto_id)


@router.post("/", response_model=ProductoResponse)
async def crear_producto(producto: ProductoCreate):
    """
    Crea un nuevo producto.
    """
    return await controller.crear_producto(producto)


@router.put("/{producto_id}", response_model=ProductoResponse)
async def actualizar_producto(producto_id: int, data: ProductoUpdate):
    """
    Actualiza un producto existente.
    """
    return await controller.actualizar_producto(producto_id, data)


@router.delete("/{producto_id}", response_model=bool)
async def eliminar_producto(producto_id: int):
    """
    Elimina un producto por ID.
    """
    return await controller.eliminar_producto(producto_id)


@router.put("/{producto_id}/ajustar-stock", response_model=ProductoResponse)
async def ajustar_stock(producto_id: int, cantidad: int = Body(...)):
    """
    Ajusta el stock del producto.
    """
    return await controller.ajustar_stock(producto_id, cantidad)


@router.post("/{producto_id}/venta")
async def registrar_venta(producto_id: int):
    """
    Registra una venta del producto con el ID proporcionado.
    """
    return await controller.registrar_venta(producto_id)
