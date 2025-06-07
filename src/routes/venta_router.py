"""
Router para endpoints CRUD de ventas.
"""

from typing import List, Optional

from fastapi import APIRouter, Query

from src.controllers.venta_controller import VentaController
from src.services.venta_service import VentaService
from src.models.venta import Venta

router = APIRouter()

# Inyección manual de dependencias
service = VentaService()
controller = VentaController(service)


@router.get("/", response_model=List[Venta])
async def listar_ventas(
    cliente: Optional[str] = Query(None, description="Filtro por nombre de cliente")
):
    """
    Retorna todas las ventas, opcionalmente filtradas por cliente.

    Args:
        cliente (Optional[str]): Cadena para filtrar por cliente.

    Returns:
        List[Venta]: Ventas encontradas.
    """
    return controller.listar_ventas(cliente)


@router.get("/{venta_id}", response_model=Venta)
async def obtener_venta(venta_id: int):
    """
    Retorna una venta dada su ID.

    Args:
        venta_id (int): ID de la venta a obtener.

    Returns:
        Venta: Venta encontrada o lanza 404 si no existe.
    """
    return controller.obtener_venta(venta_id)


@router.post("/", response_model=Venta)
async def crear_venta(venta_data: dict):
    """
    Crea una nueva venta con los datos proporcionados.

    Args:
        venta_data (dict): Diccionario con los campos de la venta.

    Returns:
        Venta: Venta creada.
    """
    return controller.crear_venta(venta_data)


@router.delete("/{venta_id}", response_model=bool)
async def eliminar_venta(venta_id: int):
    """
    Elimina una venta por su ID.

    Args:
        venta_id (int): ID de la venta a eliminar.

    Returns:
        bool: True si se eliminó, False si no se encontró.
    """
    return controller.eliminar_venta(venta_id)
