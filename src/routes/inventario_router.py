"""
Router de inventario. Expone endpoints relacionados con el stock de productos,
como listar productos con stock bajo o agotados.
"""

from typing import List
from fastapi import APIRouter, Query, HTTPException


from src.controllers.inventario_controller import InventarioController
from src.schemas.producto_schema import ProductoResponse

router = APIRouter()
controller = InventarioController()


@router.get(
    "/bajo-stock",
    response_model=List[ProductoResponse],
    summary="Listar productos con stock bajo"
)
async def listar_productos_stock_bajo(
    umbral: int = Query(5, ge=1, description="Stock máximo permitido")
) -> List[ProductoResponse]:
    """
    Retorna los productos cuyo stock es menor o igual al umbral indicado.

    Args:
        umbral (int): Umbral máximo de stock para considerar el producto como bajo.

    Returns:
        List[ProductoResponse]: Lista de productos con bajo stock.
    """
    try:
        productos = controller.listar_productos_stock_bajo(umbral)
        return [ProductoResponse.from_orm(p) for p in productos]
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Error interno al listar productos con stock bajo"
        ) from exc


@router.get(
    "/agotados",
    response_model=List[ProductoResponse],
    summary="Listar productos agotados"
)
async def listar_productos_agotados() -> List[ProductoResponse]:
    """
    Retorna los productos cuyo stock es igual a cero (agotados).

    Returns:
        List[ProductoResponse]: Lista de productos agotados.
    """
    try:
        productos = controller.listar_productos_agotados()
        return [ProductoResponse.from_orm(p) for p in productos]
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Error interno al listar productos agotados"
        ) from exc
