"""
Módulo de rutas para manejar las solicitudes HTTP relacionadas con el inventario.

Define endpoints para operaciones como el cálculo de precio de venta, total de stock disponible
y productos con bajo nivel de stock.
"""

# Importaciones estándar
from typing import List

# Importaciones de terceros
from fastapi import APIRouter, Query

# Importaciones locales
from src.controllers.inventario_controller import InventarioController
from src.models.producto import Producto
from src.services.inventario_service import InventarioService

router = APIRouter()
controller = InventarioController(service=InventarioService())


@router.get("/inventario/precio-venta", response_model=float)
async def calcular_precio_venta(
    costo: float = Query(..., description="Costo base del producto"),
    margen: float = Query(0.30, description="Margen de ganancia (por defecto 0.30)"),
) -> float:
    """
    Calcula el precio de venta sugerido a partir del costo y margen de ganancia.

    Args:
        costo (float): Costo del producto.
        margen (float): Margen de ganancia deseado (opcional).

    Returns:
        float: Precio de venta sugerido.
    """
    return controller.calcular_precio_venta(costo, margen)


@router.get("/inventario/stock-total", response_model=int)
async def obtener_stock_total() -> int:
    """
    Devuelve la cantidad total de productos disponibles en stock.

    Returns:
        int: Total de unidades en stock.
    """
    return controller.obtener_stock_total()


@router.get("/inventario/bajo-stock", response_model=List[Producto])
async def productos_bajo_stock(
    umbral: int = Query(5, description="Stock mínimo para considerar bajo")
) -> List[Producto]:
    """
    Devuelve una lista de productos cuyo stock está por debajo del umbral.

    Args:
        umbral (int): Valor límite inferior de stock. Por defecto es 5.

    Returns:
        List[Producto]: Productos con stock bajo.
    """
    return controller.obtener_productos_bajo_stock(umbral)
