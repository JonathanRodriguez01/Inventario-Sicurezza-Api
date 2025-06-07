"""
Rutas absolutas o relativas para archivos JSON.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RUTA_PRODUCTOS = os.path.join(BASE_DIR, "productos.json")
RUTA_VENTAS = os.path.join(BASE_DIR, "ventas.json")
