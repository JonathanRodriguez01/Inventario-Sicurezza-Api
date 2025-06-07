"""
Router principal que agrupa los subrouters de la API.

Este módulo centraliza las rutas importadas desde los módulos de productos, inventario y ventas,
facilitando su integración dentro de la instancia principal de FastAPI.
"""

# Importaciones de terceros
from fastapi import APIRouter

# Importaciones locales
from src.routes.producto_router import router as producto_router
from src.routes.inventario_router import router as inventario_router
from src.routes.venta_router import router as venta_router  # NUEVO

api_router = APIRouter()

# Incluir el subrouter de productos
api_router.include_router(
    producto_router,
    prefix="/productos",
    tags=["Productos"]
)

# Incluir el subrouter de inventario
api_router.include_router(
    inventario_router,
    prefix="/inventario",
    tags=["Inventario"]
)

# Incluir el subrouter de ventas
api_router.include_router(
    venta_router,
    prefix="/ventas",
    tags=["Ventas"]
)
