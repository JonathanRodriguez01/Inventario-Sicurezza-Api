"""
Controlador para manejar operaciones CRUD, búsquedas y cálculo de ganancia de productos.
"""
import io
import csv
from typing import List, Optional

from fastapi.responses import StreamingResponse
from fastapi import APIRouter, HTTPException, Query

from data.rutas import RUTA_PRODUCTOS
from helpers.json_utils import read_json_file, write_json_file
from helpers.logger import logger
from models.producto import Producto

router = APIRouter()


def leer_productos() -> List[Producto]:
    """
    Lee los productos desde el archivo JSON y devuelve instancias de Producto.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        return [Producto(**p) for p in productos_dict]
    except FileNotFoundError:
        logger.warning(
            "Archivo de productos no encontrado, retornando lista vacía."
        )
        return []
    except Exception as e:
        logger.error("Error leyendo productos: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno leyendo productos"
        ) from e


def guardar_productos(productos: List[Producto]) -> None:
    """
    Guarda la lista de productos en el archivo JSON.
    """
    try:
        write_json_file(RUTA_PRODUCTOS, [p.dict() for p in productos])
    except Exception as e:
        logger.error("Error guardando productos: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno guardando productos"
        ) from e


@router.get(
    "/exportar/csv",
    summary="Exportar todos los productos en CSV"
)
def exportar_productos_csv() -> StreamingResponse:
    """
    Genera un CSV con todos los productos y devuelve un streaming response
    para descargarlo.
    """
    productos = leer_productos()

    # Creamos un buffer en memoria
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    # Escribimos la cabecera
    writer.writerow([
        "id",
        "nombre",
        "descripcion",
        "precio_costo",
        "precio_venta",
        "stock",
        "unidades_vendidas"
    ])
    # Escribimos las filas
    for p in productos:
        writer.writerow([
            p.id,
            p.nombre,
            p.descripcion,
            p.precio_costo,
            p.precio_venta,
            p.stock,
            getattr(p, "unidades_vendidas", 0)
        ])

    # Retrocedemos el cursor del buffer
    buffer.seek(0)

    # Devolvemos como streaming response
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=productos.csv"
        }
    )

@router.get(
    "/buscar",
    response_model=List[Producto],
    summary="Buscar productos por nombre"
)
def buscar_productos_por_nombre(
    nombre: str = Query(
        ...,
        min_length=1,
        description="Nombre o parte del nombre a buscar"
    )
) -> List[Producto]:
    """
    Busca productos cuyo nombre contenga la cadena indicada (case-insensitive).
    """
    productos = leer_productos()
    resultados = [
        p for p in productos
        if nombre.lower() in p.nombre.lower()
    ]
    if not resultados:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron productos con ese nombre"
        )
    return resultados

@router.get(
    "/filtrar",
    response_model=List[Producto],
    summary="Filtro avanzado de productos"
)
def filtrar_productos(
    nombre: Optional[str] = Query(
        None,
        min_length=1,
        description="Texto parcial a buscar en el nombre"
    ),
    precio_min: Optional[float] = Query(
        None,
        ge=0,
        description="Precio de venta mínimo"
    ),
    precio_max: Optional[float] = Query(
        None,
        ge=0,
        description="Precio de venta máximo"
    ),
    stock_min: Optional[int] = Query(
        None,
        ge=0,
        description="Stock mínimo"
    )
) -> List[Producto]:
    """
    Filtra productos según los criterios proporcionados.
    Todos los parámetros son opcionales; si no se provee uno,
    no se aplica ese filtro.
    """
    productos = leer_productos()
    resultados = []

    for p in productos:
        if nombre and nombre.lower() not in p.nombre.lower():
            continue
        if precio_min is not None and p.precio_venta < precio_min:
            continue
        if precio_max is not None and p.precio_venta > precio_max:
            continue
        if stock_min is not None and p.stock < stock_min:
            continue
        resultados.append(p)

    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron productos con ese criterio")
    return resultados

@router.get(
    "/{producto_id}/ganancia",
    summary="Calcular ganancia total de un producto"
)
def calcular_ganancia_producto(producto_id: int) -> dict:
    """
    Calcula la ganancia total generada por un producto en base a unidades vendidas.
    """
    productos = leer_productos()
    for p in productos:
        if p.id == producto_id:
            ganancia_unitaria = p.precio_venta - p.precio_costo
            ganancia_total = p.unidades_vendidas * ganancia_unitaria
            return {
                "producto": p.nombre,
                "ganancia_total": round(ganancia_total, 2),
                "unidades_vendidas": p.unidades_vendidas
            }
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@router.get(
    "/",
    response_model=List[Producto],
    summary="Listar todos los productos"
)
def listar_productos() -> List[Producto]:
    """
    Endpoint para obtener todos los productos.
    """
    return leer_productos()


@router.get(
    "/{producto_id}",
    response_model=Producto,
    summary="Obtener producto por ID"
)
def obtener_producto(producto_id: int) -> Producto:
    """
    Endpoint para obtener un producto por su ID.
    """
    productos = leer_productos()
    for p in productos:
        if p.id == producto_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@router.post(
    "/",
    response_model=Producto,
    status_code=201,
    summary="Crear nuevo producto"
)
def crear_producto(producto: Producto) -> Producto:
    """
    Endpoint para crear un nuevo producto con ID generado automáticamente.
    """
    productos = leer_productos()
    nuevo_id = max((p.id for p in productos), default=0) + 1
    producto.id = nuevo_id
    productos.append(producto)
    guardar_productos(productos)
    logger.info("Producto creado: %s (ID %d)", producto.nombre, producto.id)
    return producto


@router.put(
    "/{producto_id}",
    response_model=Producto,
    summary="Actualizar producto existente"
)
def actualizar_producto(
    producto_id: int,
    producto_actualizado: Producto
) -> Producto:
    """
    Endpoint para actualizar un producto por su ID.
    """
    productos = leer_productos()
    for i, p in enumerate(productos):
        if p.id == producto_id:
            producto_actualizado.id = producto_id
            productos[i] = producto_actualizado
            guardar_productos(productos)
            logger.info(
                "Producto actualizado: %s (ID %d)",
                producto_actualizado.nombre,
                producto_id
            )
            return producto_actualizado
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@router.delete(
    "/{producto_id}",
    status_code=204,
    summary="Eliminar producto por ID"
)
def eliminar_producto(producto_id: int) -> None:
    """
    Endpoint para eliminar un producto por su ID.
    """
    productos = leer_productos()
    nuevos = [p for p in productos if p.id != producto_id]
    if len(nuevos) == len(productos):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    guardar_productos(nuevos)
    logger.info("Producto eliminado: ID %d", producto_id)


@router.get(
    "/{producto_id}/ganancia-porcentaje",
    summary="Calcular porcentaje de ganancia unitaria de un producto"
)
def calcular_porcentaje_ganancia(producto_id: int) -> dict:
    """
    Calcula el porcentaje de ganancia unitaria de un producto.

    Fórmula: (precio_venta - precio_costo) / precio_costo * 100

    Retorna:
        dict: {
            "producto": nombre,
            "ganancia_unitaria": valor,
            "porcentaje_ganancia": porcentaje_en_valor
        }
    """
    productos = leer_productos()
    for p in productos:
        if p.id == producto_id:
            ganancia_unitaria = p.precio_venta - p.precio_costo
            try:
                porcentaje = (ganancia_unitaria / p.precio_costo) * 100
            except ZeroDivisionError:
                porcentaje = 0.0
            return {
                "producto": p.nombre,
                "ganancia_unitaria": round(ganancia_unitaria, 2),
                "porcentaje_ganancia": round(porcentaje, 2)
            }
    raise HTTPException(status_code=404, detail="Producto no encontrado")
