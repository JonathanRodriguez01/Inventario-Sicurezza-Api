"""
Repositorio para la gestión de ventas.

Este módulo contiene funciones para leer, guardar y eliminar datos de ventas
desde un archivo JSON. El repositorio es responsable únicamente del acceso
y persistencia de datos.
"""

import json
from typing import List, Optional
from pathlib import Path
from src.models.venta import Venta
from src.config.settings import settings


class VentaRepository:
    """
    Clase encargada de interactuar con el origen de datos de ventas.
    """

    def __init__(self) -> None:
        """
        Inicializa el repositorio cargando el archivo de ventas desde la ruta configurada.
        """
        self.ventas_path = Path(settings.VENTAS_PATH)
        self.ventas = self._cargar_ventas()

    def _cargar_ventas(self) -> List[Venta]:
        """
        Carga las ventas desde el archivo JSON.

        Returns:
            List[Venta]: Lista de ventas cargadas.
        """
        if not self.ventas_path.exists():
            return []
        with open(self.ventas_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Venta(**venta) for venta in data]

    def _guardar_ventas(self) -> None:
        """
        Guarda la lista de ventas en el archivo JSON.
        """
        with open(self.ventas_path, "w", encoding="utf-8") as f:
            json.dump([venta.dict() for venta in self.ventas], f, ensure_ascii=False, indent=4)

    def obtener_todas_las_ventas(self) -> List[Venta]:
        """
        Retorna todas las ventas almacenadas.

        Returns:
            List[Venta]: Lista completa de ventas.
        """
        return self.ventas

    def obtener_venta_por_id(self, venta_id: int) -> Optional[Venta]:
        """
        Busca una venta por su ID.

        Args:
            venta_id (int): ID de la venta a buscar.

        Returns:
            Optional[Venta]: Venta si se encuentra, None en caso contrario.
        """
        for venta in self.ventas:
            if venta.id == venta_id:
                return venta
        return None

    def obtener_ventas_filtradas(self, cliente: str) -> List[Venta]:
        """
        Filtra ventas por nombre parcial del cliente.

        Args:
            cliente (str): Subcadena del nombre del cliente.

        Returns:
            List[Venta]: Lista de ventas que coinciden con el filtro.
        """
        return [
            venta for venta in self.ventas
            if cliente.lower() in venta.cliente.lower()
        ]

    def guardar_venta(self, venta: Venta) -> Venta:
        """
        Agrega una nueva venta y la guarda.

        Args:
            venta (Venta): Venta a agregar.

        Returns:
            Venta: Venta creada.
        """
        venta.id = len(self.ventas) + 1
        self.ventas.append(venta)
        self._guardar_ventas()
        return venta

    def eliminar_venta_por_id(self, venta_id: int) -> bool:
        """
        Elimina una venta por su ID.

        Args:
            venta_id (int): ID de la venta a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        for i, venta in enumerate(self.ventas):
            if venta.id == venta_id:
                del self.ventas[i]
                self._guardar_ventas()
                return True
        return False
