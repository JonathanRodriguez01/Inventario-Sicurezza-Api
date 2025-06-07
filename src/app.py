"""
Archivo principal de configuración de la aplicación FastAPI.

Define y configura la instancia de FastAPI, incluyendo los routers principales.
"""

from fastapi import FastAPI

from src.routes.api_router import api_router

app = FastAPI(
    title="Inventario Sicurezza API",
    description="API para gestionar productos, ventas y analizar rentabilidad.",
    version="1.0.0",
)

# Incluir todos los routers desde el router principal
app.include_router(api_router)
