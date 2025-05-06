def actualizar_producto():
        try:
            producto = input("Ingrese el producto a actualizar: ").strip()
            if producto not in inventario:
                raise KeyError("¡Producto no encontrado!")
            cantidad = int(input(f"Nuevo stock para '{producto}': "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            inventario[producto] = cantidad
            print(f"Stock de '{producto}' actualizado a {cantidad}.")
        except KeyError as e:
            print(f"Error: {e}. Intente nuevamente.")
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")