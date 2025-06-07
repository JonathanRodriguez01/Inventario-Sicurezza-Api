"""
Configuración básica de logging para la aplicación.
"""

import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Logger global de la aplicación
logger = logging.getLogger("inventario_app")
