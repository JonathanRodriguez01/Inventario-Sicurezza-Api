"""
Router para endpoints CRUD de productos.
"""

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from src.controllers.producto_controller import ProductoController
from src.repositories.producto_repository import ProductoRepository
from src.services.producto_service import ProductoService
from src.schemas.producto_schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse,
)

router = APIRouter()

# Inyección manual de dependencias
repo = ProductoRepository()
service = ProductoService(repo)
controller = ProductoController(service)


@router.get("/", response_model=List[ProductoResponse])
async def listar_productos(
    nombre: Optional[str] = Query(None, description="Filtro por nombre parcial")
):
    """
    Retorna la lista de productos, opcionalmente filtrados por nombre parcial.

    Args:
        nombre (Optional[str]): Cadena para filtrar productos.

    Returns:
        List[ProductoResponse]: Productos encontrados.
    """
    return controller.listar_productos(nombre)


@router.get("/{producto_id}", response_model=ProductoResponse)
async def obtener_producto(producto_id: int):
    """
    Retorna un producto dado su ID.

    Args:
        producto_id (int): ID del producto a obtener.

    Raises:
        HTTPException: Si no existe el producto (404).

    Returns:
        ProductoResponse: Producto encontrado.
    """
    prod = controller.obtener_producto(producto_id)
    if prod is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod


@router.post("/", response_model=ProductoResponse)
async def crear_producto(producto: ProductoCreate):
    """
    Crea un nuevo producto con los datos proporcionados.

    Args:
        producto (ProductoCreate): Datos del producto a crear.

    Returns:
        ProductoResponse: Producto creado.
    """
    return controller.crear_producto(producto)


@router.put("/{producto_id}", response_model=ProductoResponse)
async def actualizar_producto(
    producto_id: int,
    producto: ProductoUpdate
):
    """
    Actualiza un producto existente con nuevos datos.

    Args:
        producto_id (int): ID del producto a actualizar.
        producto (ProductoUpdate): Nuevos datos del producto.

    Returns:
        ProductoResponse: Producto actualizado.
    """
    return controller.actualizar_producto(producto_id, producto)


@router.delete("/{producto_id}", response_model=bool)
async def eliminar_producto(producto_id: int):
    """
    Elimina un producto por su ID.

    Args:
        producto_id (int): ID del producto a eliminar.

    Returns:
        bool: True si se eliminó correctamente, False si no se encontró.
    """
    return controller.eliminar_producto(producto_id)
