def mostrar_menu_principal():
    print("\n--- MENÚ DE CINE ATENAS ---")
    print("1. Promociones")
    print("2. Bebidas")
    print("3. Bocadillos")
    print("4. Asientos")
    print("5. Finalizar compra")

def mostrar_items(lista):
    for item in lista:
        print(item)

def agregar_producto(lista_texto, lista_precios, resumen, precios_seleccionados):
    while True:
        mostrar_items(lista_texto)
        try:
            opcion = int(input("Seleccione un número (0 para regresar): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(lista_texto):
                resumen.append(lista_texto[opcion - 1])
                precios_seleccionados.append(lista_precios[opcion - 1])
                print("Producto agregado.")
            else:
                print("Opción invalida. Intente de nuevo.")
        except ValueError:
            print("!Entrada invalida!. la opcion solo debe ser un numero.")
    return

def finalizar_compra(resumen, precios):
    print("\n----- CINEMAS ATENAS -----")
    print("Productos comprados:")
    for item in resumen:
        print("-", item)
    total = sum(precios)
    print(f"\nTOTAL A PAGAR: {total}c$")
    print("¡Gracias por su compra!")

def menu_cine_atenas():
    promociones = ["1. Palomitas yumbo = 70c$", "2. Palomitas mediana + bebida grande = 130c$"]
    precios_promo = [70, 130]

    bebidas = [
        "1. Bebida carbonatada yumbo = 80c$",
        "2. Bebida carbonatada mediana = 60c$",
        "3. Bebida carbonatada pequeña = 40c$",
        "4. Jugos medianos = 40c$",
        "5. Jugos pequeños = 32c$",
        "6. Agua = 30c$"
    ]
    precios_bebidas = [80, 60, 40, 40, 32, 30]

    bocadillos = [
        "1. Palomitas yumbo = 90c$",
        "2. Palomitas medianas = 70c$",
        "3. Palomitas pequeñas = 50c$",
        "4. Nachos = 65c$",
        "5. Golosinas = 25c$"
    ]
    precios_bocadillos = [90, 70, 50, 65, 25]

    asientos = [
        "1. Boleto VIP = 700c$",
        "2. Boleto normal = 200c$",
        "3. Lentes 3D = 100c$"
    ]
    precios_asientos = [700, 200, 100]

    resumen = []
    precios_seleccionados = []

    while True:
        mostrar_menu_principal()
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                agregar_producto(promociones, precios_promo, resumen, precios_seleccionados)
            elif opcion == 2:
                agregar_producto(bebidas, precios_bebidas, resumen, precios_seleccionados)
            elif opcion == 3:
                agregar_producto(bocadillos, precios_bocadillos, resumen, precios_seleccionados)
            elif opcion == 4:
                agregar_producto(asientos, precios_asientos, resumen, precios_seleccionados)
            elif opcion == 5:
                finalizar_compra(resumen, precios_seleccionados)
                break
            else:
                print("Opción invalida. Intente de nuevo.")
        except ValueError:
            print(" X  Entrada invalida. Intente con un numero.  X")

# Ejecutar el programa
menu_cine_atenas()
