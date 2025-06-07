# Inventario Sicurezza API

API desarrollada con FastAPI para la gestión de productos, inventario y ventas. Permite registrar productos, realizar operaciones de inventario y consultar ventas, todo a través de endpoints RESTful bien organizados por capas.

---

## 📁 Estructura del proyecto

├── data/
│ ├── productos.json
│ └── ventas.json
├── src/
│ ├── app.py
│ ├── settings.py
│ ├── helpers/
│ │ ├── json_utils.py
│ │ └── logger.py
│ ├── models/
│ │ ├── producto.py
│ │ ├── venta.py
│ │ └── inventario.py
│ ├── schemas/
│ │ ├── producto_schema.py
│ │ ├── venta_schema.py
│ │ └── inventario_schema.py
│ ├── repositories/
│ │ ├── producto_repository.py
│ │ ├── venta_repository.py
│ │ └── inventario_repository.py
│ ├── services/
│ │ ├── producto_service.py
│ │ ├── venta_service.py
│ │ └── inventario_service.py
│ ├── controllers/
│ │ ├── producto_controller.py
│ │ ├── venta_controller.py
│ │ └── inventario_controller.py
│ └── routes/
│ ├── api_router.py
│ ├── producto_router.py
│ ├── venta_router.py
│ └── inventario_router.py
├── .env
├── .env.example
├── requirements.txt
└── master.py

---

## 🚀 Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/Inventario-Sicurezza-Api.git
cd Inventario-Sicurezza-Api

2. **Crear y activar entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. **Instalar dependencias**

```bash
pip install -r requirements.txt

4. **Crear archivo .env**

Puedes usar el archivo .env.example como base:

```bash
cp .env.example .env

5. **Ejecutar la API**

```bash
python master.py

---

## ⚙️ Variables de entorno

El archivo .env debe contener:

PRODUCTOS_PATH=data/productos.json
VENTAS_PATH=data/ventas.json
HOST=127.0.0.1
PORT=8000

## 📫 Endpoints principales

Una vez en ejecución, puedes acceder a la documentación interactiva:

• Swagger: http://127.0.0.1:8000/docs

• Redoc: http://127.0.0.1:8000/redoc

Productos

GET /productos/
GET /productos/{id}
POST /productos/
PUT /productos/{id}
DELETE /productos/{id}

Inventario

GET /inventario/
GET /inventario/{id}
POST /inventario/
PUT /inventario/{id}
DELETE /inventario/{id}

---

## 📦 Requisitos (requirements.txt)

fastapi
uvicorn
pydantic
pydantic-settings

👨‍💻 Autor
Jonathan Daniel Rodríguez

## 📄 Licencia
Este proyecto se encuentra bajo licencia MIT. Puedes usarlo libremente para fines educativos.