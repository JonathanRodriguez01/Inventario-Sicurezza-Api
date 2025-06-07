"""
Servicio para operaciones relacionadas con ventas.

Gestiona la lectura, creación y eliminación de ventas usando JSON como almacenamiento.
"""

from typing import List, Optional

from src.models.venta import Venta
from src.helpers.json_utils import leer_json, escribir_json
from src.config.settings import settings


class VentaService:
    """Servicio que maneja la lógica de negocio para ventas."""

    def __init__(self):
        """
        Inicializa el servicio con la ruta al archivo de ventas definida en settings.
        """
        self.ruta_ventas = settings.ventas_path

    def listar_ventas(self, cliente: Optional[str] = None) -> List[Venta]:
        """
        Lee todas las ventas y opcionalmente filtra por nombre de cliente.

        Args:
            cliente (Optional[str]): Nombre parcial para filtrar ventas.

        Returns:
            List[Venta]: Lista de instancias Venta.
        """
        ventas_data = leer_json(self.ruta_ventas)
        ventas = [Venta(**v) for v in ventas_data]
        if cliente:
            return [v for v in ventas if cliente.lower() in v.cliente.lower()]
        return ventas

    def obtener_venta(self, venta_id: int) -> Venta:
        """
        Busca una venta por su ID.

        Args:
            venta_id (int): ID de la venta.

        Raises:
            ValueError: Si no se encuentra la venta.

        Returns:
            Venta: Venta encontrada.
        """
        ventas_data = leer_json(self.ruta_ventas)
        for v in ventas_data:
            if v.get("id") == venta_id:
                return Venta(**v)
        raise ValueError("Venta no encontrada")

    def crear_venta(self, venta_data: dict) -> Venta:
        """
        Crea una nueva venta y la guarda en el almacenamiento JSON.

        Args:
            venta_data (dict): Datos de la venta a crear.

        Returns:
            Venta: Venta recién creada.
        """
        ventas_data = leer_json(self.ruta_ventas)
        nuevo_id = max([v["id"] for v in ventas_data], default=0) + 1
        venta_data["id"] = nuevo_id
        ventas_data.append(venta_data)
        escribir_json(self.ruta_ventas, ventas_data)
        return Venta(**venta_data)

    def eliminar_venta(self, venta_id: int) -> bool:
        """
        Elimina una venta por su ID.

        Args:
            venta_id (int): ID de la venta a eliminar.

        Returns:
            bool: True si se eliminó, False si no existía.
        """
        ventas_data = leer_json(self.ruta_ventas)
        nuevas_ventas = [v for v in ventas_data if v.get("id") != venta_id]
        if len(nuevas_ventas) == len(ventas_data):
            return False
        escribir_json(self.ruta_ventas, nuevas_ventas)
        return True
