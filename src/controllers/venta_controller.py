"""
Controlador de lógica de negocio para ventas.

Este controlador actúa de intermediario entre las rutas y el servicio de ventas,
capturando excepciones y traduciéndolas en HTTPException adecuadas.
"""

from typing import List, Optional

from fastapi import HTTPException

from src.models.venta import Venta
from src.services.venta_service import VentaService


class VentaController:
    """Controlador que gestiona las operaciones CRUD sobre ventas."""

    def __init__(self, service: VentaService):
        """
        Inicializa el controlador con el servicio de ventas.

        Args:
            service (VentaService): Servicio que maneja la lógica de ventas.
        """
        self.service = service

    def listar_ventas(self, cliente: Optional[str] = None) -> List[Venta]:
        """
        Lista todas las ventas, opcionalmente filtradas por nombre de cliente.

        Args:
            cliente (Optional[str]): Nombre parcial para filtrar ventas.

        Returns:
            List[Venta]: Lista de ventas.
        """
        return self.service.listar_ventas(cliente)

    def obtener_venta(self, venta_id: int) -> Venta:
        """
        Obtiene una venta por su ID.

        Args:
            venta_id (int): ID de la venta a obtener.

        Raises:
            HTTPException: Si la venta no existe (404).

        Returns:
            Venta: Venta encontrada.
        """
        try:
            return self.service.obtener_venta(venta_id)
        except ValueError as exc:
            raise HTTPException(
                status_code=404,
                detail="Venta no encontrada"
            ) from exc

    def crear_venta(self, venta_data: dict) -> Venta:
        """
        Crea una nueva venta con los datos proporcionados.

        Args:
            venta_data (dict): Diccionario con los campos de la venta.

        Returns:
            Venta: Venta creada.
        """
        return self.service.crear_venta(venta_data)

    def eliminar_venta(self, venta_id: int) -> bool:
        """
        Elimina una venta por su ID.

        Args:
            venta_id (int): ID de la venta a eliminar.

        Raises:
            HTTPException: Si la venta no existe (404).

        Returns:
            bool: True si se eliminó correctamente.
        """
        eliminado = self.service.eliminar_venta(venta_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Venta no encontrada")
        return True
