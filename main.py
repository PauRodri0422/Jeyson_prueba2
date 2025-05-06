from agregar import agregar_producto 
from actualizar import actualizar_producto
from eliminar import eliminar_producto
from mostrar import mostrar_inventario



inventario = {
       "Pera" : 20,
       "Ciruela" : 50,
       "Pitaya" : 45,
       "zapote" : 30,
       "Fresas" : 60,
       "arandanos" : 25}


def gestionar_inventario(inventario):
    agregar_producto()
    actualizar_producto()
    eliminar_producto()
    mostrar_inventario()
    
    opciones = {
        "1": actualizar_producto,
        "2": agregar_producto,
        "3": eliminar_producto,
        "4": lambda: print("Gestión de inventario terminada.")
    }

    while True:
        mostrar_inventario()
        print("\nOpciones:")
        print("1. Modificar stock de un producto")
        print("2. Agregar nuevo producto")
        print("3. Eliminar producto")
        print("4. Terminar")

        opcion = input("\nSeleccione una opción (1-4): ").strip()
        if opcion in opciones:
            if opcion == "4":
                break
            opciones[opcion]()
        else:
            print("Opción no válida. Intente nuevamente.")

    return inventario

# Uso de la función
inventario_actualizado = gestionar_inventario(inventario)
print("\nInventario final:", inventario_actualizado)