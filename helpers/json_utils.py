"""
Funciones utilitarias para leer y escribir archivos JSON.
"""

import json
from typing import Any
from helpers.logger import logger

def read_json_file(path: str) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning("Archivo JSON no encontrado en %s, retornando lista vacía", path)
        return []
    except json.JSONDecodeError as e:
        logger.error("Error decodificando JSON en %s: %s", path, e)
        raise
    except Exception as e:
        logger.error("Error leyendo archivo JSON %s: %s", path, e)
        raise

def write_json_file(path: str, data: Any) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error("Error escribiendo archivo JSON %s: %s", path, e)
        raise
