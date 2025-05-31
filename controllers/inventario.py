"""
Controlador para gestión de ventas y generación de ranking por ganancia.
"""

from collections import defaultdict

from fastapi import APIRouter, HTTPException, Query

from models.venta import Venta
from models.producto import Producto
from helpers.json_utils import read_json_file, write_json_file
from helpers.logger import logger
from data.rutas import RUTA_PRODUCTOS, RUTA_VENTAS

router = APIRouter()

@router.post(
    "/ventas",
    response_model=dict,
    summary="Registrar una venta"
)
def registrar_venta(venta: Venta) -> dict:
    """
    Registra una venta de producto y guarda la información.

    Actualiza únicamente el registro de ventas.
    """
    try:
        productos = read_json_file(RUTA_PRODUCTOS)
        ventas = read_json_file(RUTA_VENTAS)
    except Exception as e:
        logger.error("Error leyendo archivos de datos: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno leyendo datos"
        ) from e

    producto = next(
        (p for p in productos if p.get("id") == venta.producto_id),
        None
    )
    if not producto:
        logger.warning("Producto con ID %d no encontrado", venta.producto_id)
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto.get("stock", 0) < venta.cantidad_vendida:
        logger.warning(
            "Stock insuficiente para producto ID %d", venta.producto_id
        )
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    ventas.append(venta.dict())

    try:
        write_json_file(RUTA_VENTAS, ventas)
    except Exception as e:
        logger.error("Error guardando archivo de ventas: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno al guardar la venta"
        ) from e

    logger.info(
        "Venta registrada: %d unidades del producto ID %d",
        venta.cantidad_vendida,
        venta.producto_id
    )
    return {"mensaje": "Venta registrada exitosamente"}

@router.get(
    "/ventas/top",
    response_model=list,
    summary="Obtener productos más vendidos por ganancia"
)
def productos_mas_vendidos() -> list:
    """
    Devuelve un ranking de productos ordenados por ganancia total.

    La ganancia se calcula como cantidad_vendida * (precio_venta - precio_costo).
    """
    try:
        ventas = read_json_file(RUTA_VENTAS)
        productos = read_json_file(RUTA_PRODUCTOS)
    except Exception as e:
        logger.error("Error leyendo archivos de datos: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno leyendo datos"
        ) from e

    resumen = defaultdict(
        lambda: {"nombre": "", "unidades": 0, "ganancia_total": 0.0}
    )

    for venta in ventas:
        producto = next(
            (p for p in productos if p.get("id") == venta.get("producto_id")),
            None
        )
        if producto:
            pid = producto.get("id")
            resumen[pid]["nombre"] = producto.get("nombre")
            unidades = venta.get("cantidad_vendida", 0)
            resumen[pid]["unidades"] += unidades
            ganancia_unitaria = (
                producto.get("precio_venta", 0) - producto.get("precio_costo", 0)
            )
            resumen[pid]["ganancia_total"] += unidades * ganancia_unitaria

    resultado = sorted(
        resumen.items(),
        key=lambda x: x[1].get("ganancia_total", 0),
        reverse=True
    )

    return [{"id": pid, **data} for pid, data in resultado]

@router.get(
    "/ganancia-total",
    summary="Calcular la ganancia total del inventario vendido"
)
def obtener_ganancia_total() -> dict:
    """
    Calcula la ganancia total generada por las ventas realizadas.

    Retorna:
        dict: Un diccionario con la ganancia total acumulada.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**prod) for prod in productos_dict]

        ganancia_total = sum(
            (p.precio_venta - p.precio_costo) * p.unidades_vendidas for p in productos
        )

        return {"ganancia_total": round(ganancia_total, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al calcular la ganancia total") from e


@router.get(
    "/producto-mayor-stock",
    summary="Obtener el producto con mayor stock"
)
def obtener_producto_mayor_stock() -> dict:
    """
    Devuelve el producto que tiene mayor cantidad en stock.

    Retorna:
        dict: Datos del producto con mayor stock.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**p) for p in productos_dict]
    except Exception as e:
        logger.error("Error leyendo productos: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error interno leyendo productos"
        ) from e

    if not productos:
        raise HTTPException(
            status_code=404,
            detail="No hay productos en el inventario"
        )

    # Buscamos el producto con máximo stock
    mayor = max(productos, key=lambda p: p.stock)
    return {
        "id": mayor.id,
        "nombre": mayor.nombre,
        "stock": mayor.stock
    }


@router.get(
    "/stock-total",
    summary="Obtener cantidad total de unidades en stock"
)
def obtener_stock_total() -> dict:
    """
    Calcula la cantidad total de unidades disponibles en inventario.

    Retorna:
        dict: Un diccionario con la cantidad total de stock.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**prod) for prod in productos_dict]

        stock_total = sum(p.stock for p in productos)

        return {"stock_total": stock_total}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al calcular el stock total") from e

@router.get(
    "/valor-inventario",
    summary="Obtener el valor total del inventario"
)
def obtener_valor_inventario() -> dict:
    """
    Calcula el valor total del inventario en base al precio de costo y venta.

    Retorna:
        dict: Valor total a precio de costo y a precio de venta.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**prod) for prod in productos_dict]

        valor_costo = sum(p.precio_costo * p.stock for p in productos)
        valor_venta = sum(p.precio_venta * p.stock for p in productos)

        return {
            "valor_total_costo": round(valor_costo, 2),
            "valor_total_venta": round(valor_venta, 2)
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al calcular el valor del inventario"
        ) from e

@router.get(
    "/productos-agotados",
    summary="Listar productos con stock agotado"
)
def listar_productos_agotados() -> list[dict]:
    """
    Retorna los productos cuyo stock es igual a cero.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        # Convertir a modelos Pydantic para validación
        productos = [Producto(**prod) for prod in productos_dict]
        agotados = [p for p in productos if p.stock == 0]
        return [p.model_dump() for p in agotados]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener productos agotados"
        ) from e

@router.get(
    "/stock-bajo",
    summary="Listar productos con stock bajo"
)
def listar_productos_stock_bajo(
    umbral: int = Query(
        5,
        ge=1,
        description="Cantidad mínima de stock para considerar bajo"
    )
) -> list[dict]:
    """
    Retorna los productos cuyo stock es menor o igual al umbral indicado.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**prod) for prod in productos_dict]
        bajos = [p for p in productos if p.stock <= umbral]
        return [p.model_dump() for p in bajos]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener productos con stock bajo"
        ) from e

@router.get(
    "/{producto_id}/ganancia",
    summary="Calcular ganancia total de un producto"
)
def calcular_ganancia_producto(producto_id: int) -> dict:
    """
    Calcula la ganancia total generada por un producto específico según sus unidades vendidas.

    Retorna:
        dict: Contiene nombre del producto, unidades vendidas y ganancia total.
    """
    try:
        productos_dict = read_json_file(RUTA_PRODUCTOS)
        productos = [Producto(**prod) for prod in productos_dict]

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
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al calcular la ganancia del producto"
        ) from e

@router.get(
    "/ventas/producto/{producto_id}",
    summary="Obtener el historial de ventas de un producto"
)
def obtener_historial_ventas(producto_id: int) -> list[dict]:
    """
    Devuelve todas las ventas realizadas del producto con el ID proporcionado.

    Args:
        producto_id (int): ID del producto.

    Returns:
        list[dict]: Lista de ventas correspondientes al producto.
    """
    try:
        ventas = read_json_file(RUTA_VENTAS)
    except Exception as e:
        logger.error("Error al leer archivo de ventas: %s", e)
        raise HTTPException(status_code=500, detail="Error interno leyendo ventas") from e

    ventas_producto = [
        v for v in ventas if v.get("producto_id") == producto_id
    ]

    if not ventas_producto:
        raise HTTPException(status_code=404, detail="No se encontraron ventas para este producto")

    return ventas_producto
