def agregar_producto():
        try:
            producto = input("Ingrese nuevo producto: ").strip()
            if not producto:
                raise ValueError("El nombre del producto no puede estar vacío.")
            cantidad = int(input(f"Ingrese cantidad para '{producto}': "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            inventario[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")