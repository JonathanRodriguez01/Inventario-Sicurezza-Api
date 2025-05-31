"""
Punto de entrada para la API Inventario Sicurezza usando FastAPI.
"""

from fastapi import FastAPI
from dotenv import load_dotenv

from controllers.producto_controller import router as producto_router
from controllers.inventario import router as inventario_router
from config.settings import settings

# Carga variables de entorno desde .env
load_dotenv()

app = FastAPI(
    title="API Inventario Sicurezza",
    description="API para manejo completo de productos, inventario y ventas.",
    version="1.0.0",
)

# Registrar routers
app.include_router(
    producto_router,
    prefix="/productos",
    tags=["Productos"]
)
app.include_router(
    inventario_router,
    prefix="/inventario",
    tags=["Inventario"]
)


@app.get("/", summary="Ruta raíz")
def root():
    """Endpoint de bienvenida."""
    return {"mensaje": "Bienvenido a la API del Inventario Sicurezza"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
