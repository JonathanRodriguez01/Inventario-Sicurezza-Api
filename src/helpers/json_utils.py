"""
Utilidades para operaciones de lectura y escritura de archivos JSON.
"""

import json
from typing import Any


def leer_json(path: str) -> Any:
    """
    Lee un archivo JSON desde el path especificado.

    Args:
        path (str): Ruta al archivo JSON.

    Returns:
        Any: Contenido del archivo JSON parseado como objeto Python.
    """
    with open(path, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def escribir_json(path: str, data: Any) -> None:
    """
    Escribe un objeto Python en un archivo JSON en el path especificado.

    Args:
        path (str): Ruta al archivo JSON.
        data (Any): Objeto Python a serializar en formato JSON.
    """
    with open(path, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=4)
