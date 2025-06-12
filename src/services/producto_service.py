"""
Servicio para la lógica de negocio relacionada con productos.
Maneja lectura, escritura y modificación de productos en archivo JSON.
"""

import os
from fastapi import HTTPException
from src.helpers.json_utils import leer_json, escribir_json
from src.schemas.producto_schema import ProductoUpdate, ProductoResponse


class ProductoService:
    """
    Servicio de productos. Implementa la lógica CRUD y ajustes de stock.
    """

    def __init__(self):
        self.ruta_productos = os.path.join("src", "data", "productos.json")

    def listar_productos(self) -> list[ProductoResponse]:
        """
        Retorna la lista completa de productos.
        """
        productos = leer_json(self.ruta_productos)
        return [ProductoResponse(**p) for p in productos]

    def registrar_venta(self, producto_id: int) -> dict:
        """
        Registra una venta sumando +1 al campo ventas.

        Args:
            producto_id (int): ID del producto a vender.

        Returns:
            dict: Mensaje de éxito con ventas totales.
        """
        productos = leer_json(self.ruta_productos)
        for producto in productos:
            if producto["id"] == producto_id:
                producto["ventas"] = producto.get("ventas", 0) + 1
                escribir_json(self.ruta_productos, productos)
                return {
                    "mensaje": "Venta registrada",
                    "producto_id": producto_id,
                    "ventas_totales": producto["ventas"]
                }
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    def obtener_producto(self, producto_id: int) -> ProductoResponse:
        """
        Retorna un producto dado su ID.
        """
        productos = leer_json(self.ruta_productos)
        for producto in productos:
            if producto["id"] == producto_id:
                return ProductoResponse(**producto)
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    def crear_producto(self, data: dict) -> ProductoResponse:
        """
        Crea un nuevo producto con un ID único.
        """
        productos = leer_json(self.ruta_productos)
        ids = [p["id"] for p in productos]
        nuevo_id = max(ids, default=0) + 1
        data["id"] = nuevo_id
        data["ventas"] = 0
        productos.append(data)
        escribir_json(self.ruta_productos, productos)
        return ProductoResponse(**data)

    def actualizar_producto(self, producto_id: int, data: dict) -> ProductoResponse:
        """
        Actualiza los datos de un producto existente.
        """
        productos = leer_json(self.ruta_productos)
        for producto in productos:
            if producto["id"] == producto_id:
                producto.update(data)
                escribir_json(self.ruta_productos, productos)
                return ProductoResponse(**producto)
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Elimina un producto por su ID.
        """
        productos = leer_json(self.ruta_productos)
        for i, producto in enumerate(productos):
            if producto["id"] == producto_id:
                productos.pop(i)
                escribir_json(self.ruta_productos, productos)
                return True
        return False

    def ajustar_stock(self, producto_id: int, cantidad: int) -> ProductoResponse:
        """
        Suma o resta cantidad al stock del producto.
        """
        productos = leer_json(self.ruta_productos)
        for producto in productos:
            if producto["id"] == producto_id:
                nuevo_stock = producto["cantidad"] + cantidad
                if nuevo_stock < 0:
                    raise HTTPException(
                        status_code=400,
                        detail="Stock insuficiente para descontar"
                    )
                producto["cantidad"] = nuevo_stock
                escribir_json(self.ruta_productos, productos)
                return ProductoResponse(**producto)
        raise HTTPException(status_code=404, detail="Producto no encontrado")
