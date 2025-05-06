def mostrar_inventario():
        print("\nInventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")