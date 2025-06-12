"""
Router principal que agrupa los subrouters de la API.

Este módulo centraliza las rutas importadas desde los módulos de productos, inventario y ventas,
facilitando su integración dentro de la instancia principal de FastAPI.
"""

# Importaciones de terceros
from fastapi import APIRouter

# Importaciones locales
from src.routes.producto_router import router as producto_router

api_router = APIRouter()

# Incluir el subrouter de productos
api_router.include_router(
    producto_router,
    prefix="/productos",
    tags=["Productos"]
)
