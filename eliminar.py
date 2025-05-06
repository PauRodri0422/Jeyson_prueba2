def eliminar_producto():
        try:
            producto = input("Ingrese el producto a eliminar: ").strip()
            if producto not in inventario:
                raise KeyError("¡Producto no encontrado!")
            del inventario[producto]
            print(f"Producto '{producto}' eliminado.")
        except KeyError as e:
            print(f"Error: {e}. Intente nuevamente.")