from typing import List
from cliente import Cliente


# lista = arreglo = colección
lista_clientes: list[Cliente] = [ ]

# --------------- Diccionario para tarifas ---------------
TARIFAS = {
    "Particular": {
        "cita": 80000,
        "Limpieza":    60000,
        "Calzas":      80000,
        "Extracción":  100000,
        "Diagnóstico": 50000,
    },
    "EPS": {
        "cita": 5000,
        "Limpieza":    0,
        "Calzas":      40000,
        "Extracción":  40000,
        "Diagnóstico": 0,
    },
    "Prepagada": {
        "cita": 30000,
        "Limpieza":    0,
        "Calzas":      10000,
        "Extracción":  10000,
        "Diagnóstico": 0,
    },
}

# ──────────────────────────────────────────────
#  FUNCIÓN: registar_cliente
#  
# ──────────────────────────────────────────────

def registar_cliente():
    print("\n" + "─" * 50)
    print("  NUEVO CLIENTE")
    print("─" * 50)
    cedula_cliente = input("Ingrese el número de cedula: ")
    if(cedula_cliente == ""):
        print("ERROR: El campo del número de cedula no puede quedar vacío ")
    else:
        nombre_cliente = input("Ingrese nombre del cliente: ")
        telefono_cliente = input("Ingrese número de teléfono: ")

        print("Tipo de cliente: ")
        print("  1. Particular")
        print("  2. EPS")
        print("  3. Prepagada")
        tipo_cliente = input("Ingrese una oppción: ")
        if tipo_cliente == "1":
            tipo_cliente = "Particular"

        print("Tipo de atención: ")
        print("  1. Limpieza")
        print("  2. Calzas")
        print("  3. Extracción")
        print("  4. Diagnostico")
        tipo_atencion = input("Ingrese una opción: ")
        if tipo_atencion == "1":
            tipo_atencion = "Limpieza"

        print("Prioridad de atención: ")
        print("  1. Normal")
        print("  2. Urgente")
        prioridad_atencion = input("Ingrese una opcion: ")

        fecha_cita = input("Ingrese fecha de la cita (DD/MM/AAAA): ")

        cliente = Cliente()
        cliente.cedula = cedula_cliente
        cliente.nombre = nombre_cliente
        cliente.telefono = telefono_cliente
        cliente.tip_cliente = tipo_cliente
        cliente.tip_atencion = tipo_atencion
        cliente.prioridad = prioridad_atencion
        cliente.fecha = fecha_cita
        lista_clientes.append(cliente)

        #total_venta = 0
        #total_venta = TARIFAS(tipo_cliente) + TARIFAS(tipo_atencion)
        #print(f"El total de la venta es: {total_venta}")

        

# ──────────────────────────────────────────────
#  FUNCIÓN: ver_lista_clientes
#  
# ──────────────────────────────────────────────

def ver_lista_clientes():
    print("Buscar cliente")
    cliente_a_buscar = input("Ingrese el numero de cedula: ")
    cliente_encontrado = None
    for cliente in lista_clientes:
        if(cliente.cedula == cliente_a_buscar):
            cliente_encontrado = cliente

    if cliente_encontrado == None:
        print("Cliente no encontrado")
    else:
        print(f"Cliente: {cliente_encontrado.cedula}: {cliente_encontrado.nombre}")
    

    

# ──────────────────────────────────────────────
#  FUNCIÓN: menu
#  Main program.
# ──────────────────────────────────────────────

def menu():
    ciclo_menu = True    
    while ciclo_menu == True:
        print("\n" + "═" * 50)
        print("  CONSULTORIO ODONTOLÓGICO — Dr. AAA")
        print("═" * 50)
        print("  1. Registrar nuevo cliente")
        print("  2. Ver listado de clientes")
        print("  3. Ver estadísticas")
        print("  4. Salir")
        print("─" * 50)
        opcion = input("Ingrese una oipción: ")
        if opcion == "1":
            registar_cliente()
        if opcion == "2":
            ver_lista_clientes()
        if opcion == "6":
            ciclo_menu = False



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()