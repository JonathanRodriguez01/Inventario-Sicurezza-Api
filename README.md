# 🛡️ Inventario Sicurezza API

API desarrollada con **FastAPI** para gestionar productos, ventas y fomentar la toma de decisiones basada en datos de rentabilidad.

---

## 📋 Contenido

1. [Descripción](#descripción)  
2. [Requisitos](#requisitos)  
3. [Instalación](#instalación)  
4. [Configuración](#configuración)  
5. [Ejecutar la aplicación](#ejecutar-la-aplicación)  
6. [Documentación interactiva](#documentación-interactiva)  
7. [Estructura del proyecto](#estructura-del-proyecto)  
8. [Endpoints principales](#endpoints-principales)  
9. [Buenas prácticas de Git](#buenas-prácticas-de-git)  
10. [Licencia](#licencia)  

---

## 📖 Descripción

Esta API permite:

- CRUD completo de **productos** (crear, listar, obtener, actualizar, eliminar).  
- Registrar **ventas** y ajustar stock.  
- Obtener **ranking** de productos por ganancia.  
- Buscar productos por nombre y calcular ganancia unitaria/total.

---

## 🎯 Requisitos

- **Python** ≥ 3.10  
- **pip**  
- **Git**  

---

## 🚀 Instalación

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu_usuario/Inventario-Sicurezza-Api.git
   cd Inventario-Sicurezza-Api


2. **Crear y activar entorno virtual**

En Linux/Mac:

python3 -m venv venv
source venv/bin/activate

En Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


3. **Instalar dependencias**

pip install -r requirements.txt

---

## ⚙️ Configuración

1. **Copiar el archivo de ejemplo**

cp .env.example .env

---

2. **Editar .env**

PRODUCTOS_PATH=data/productos.json
VENTAS_PATH=data/ventas.json
HOST=127.0.0.1
PORT=8000

---

3.**Asegurarse de que existan los archivos JSON**

• data/productos.json

• data/ventas.json

Ambos pueden comenzar vacíos:

[]

---

## ▶️ Ejecutar la aplicación

uvicorn main:app --reload

• La bandera --reload recarga el servidor en cada cambio de código.

---

## 📑 Documentación interactiva

• Swagger UI: http://127.0.0.1:8000/docs

• ReDoc: http://127.0.0.1:8000/redoc

---

## 🗂️ Estructura del proyecto

Inventario-Sicurezza-Api/
├── config/
│   └── settings.py
├── controllers/
│   ├── producto_controller.py
│   └── inventario.py
├── data/
│   ├── productos.json
│   └── ventas.json
├── helpers/
│   ├── json_utils.py
│   └── logger.py
├── models/
│   ├── producto.py
│   └── venta.py
├── .env.example
├── .gitignore
├── main.py
└── requirements.txt

---

## 🔌 Endpoints principales

Productos

| Método | Ruta                        | Descripción                            |
| ------ | --------------------------- | -------------------------------------- |
| GET    | `/productos/`               | Listar todos los productos             |
| GET    | `/productos/{id}`           | Obtener un producto por ID             |
| POST   | `/productos/`               | Crear un producto (se genera ID)       |
| PUT    | `/productos/{id}`           | Actualizar producto por ID             |
| DELETE | `/productos/{id}`           | Eliminar producto por ID               |
| GET    | `/productos/buscar?nombre=` | Buscar productos por nombre parcial    |
| GET    | `/productos/{id}/ganancia`  | Calcular ganancia total de un producto |

Inventario / Ventas

| Método | Ruta                     | Descripción                       |
| ------ | ------------------------ | --------------------------------- |
| POST   | `/inventario/ventas`     | Registrar una venta               |
| GET    | `/inventario/ventas/top` | Ranking de productos por ganancia |

---

## 📝 Buenas prácticas de Git

• Usar ramas para nuevas funcionalidades:

git checkout -b feature/nueva-funcionalidad

• Commits descriptivos en inglés o español.

• No versionar archivos de datos internos (.gitignore ya configurado).

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT.

---

¡Listo para arrancar con tu API de Inventario Sicurezza!