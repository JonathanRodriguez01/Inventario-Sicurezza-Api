"""
Script de arranque de la aplicación FastAPI con Uvicorn.

Este archivo ejecuta la aplicación importando la instancia de FastAPI definida en app.py.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
