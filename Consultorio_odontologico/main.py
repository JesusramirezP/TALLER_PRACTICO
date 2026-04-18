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

# ── Utilidad: formato moneda colombiana ──
def fmt_cop(valor: int) -> str:          # ← AQUÍ, antes de las clases
    return f"${valor:,.0f}".replace(",", ".")

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
        if tipo_cliente == "2":
            tipo_cliente = "EPS"
        if tipo_cliente == "3":
            tipo_cliente = "Prepagada"

        print("Tipo de atención: ")
        print("  1. Limpieza")
        print("  2. Calzas")
        print("  3. Extracción")
        print("  4. Diagnostico")

        cant_procedimientos = 0
        numero_extracciones = 0

        tipo_atencion = input("Ingrese una opción: ")
        if tipo_atencion == "1":
            tipo_atencion = "Limpieza"
            cant_procedimientos = 1

        if tipo_atencion == "2":
            tipo_atencion = "Calzas"
            cant_procedimientos = int(input("Ingrese cantidad >0: "))


        if tipo_atencion == "3":
            tipo_atencion = "Extracción"
            cant_procedimientos = int(input("Ingrese cantidad >0: "))
            numero_extracciones = cant_procedimientos  # solo aquí aplica

        if tipo_atencion == "4":
            tipo_atencion = "Diagnóstico"
            cant_extraccion = 1

        print("Prioridad de atención: ")
        print("  1. Normal")
        print("  2. Urgente")
        prioridad_atencion = input("Ingrese una opcion: ")
        if prioridad_atencion == "1":
            prioridad_atencion = "Normal"
        if prioridad_atencion == "2":
            prioridad_atencion = "Urgente"

        fecha_cita = input("Ingrese fecha de la cita (DD/MM/AAAA): ")

        valor_cita = TARIFAS[tipo_cliente]["cita"]
        valor_atencion = TARIFAS[tipo_cliente][tipo_atencion]
        valor_atencion = valor_atencion * cant_procedimientos
        total_a_pagar = valor_cita + valor_atencion

        cliente = Cliente()
        cliente.cedula = cedula_cliente
        cliente.nombre = nombre_cliente
        cliente.telefono = telefono_cliente
        cliente.tip_cliente = tipo_cliente
        cliente.tip_atencion = tipo_atencion
        cliente.cantidad = cant_procedimientos
        cliente.prioridad = prioridad_atencion
        cliente.fecha = fecha_cita
        cliente.valor_cita = valor_cita
        cliente.valor_atencion = valor_atencion
        cliente.total = total_a_pagar
        cliente.cant_extraccion = numero_extracciones
        lista_clientes.append(cliente)

        

        print("\n--- RESUMEN DE PAGO ---")
        print(f"Valor cita: ${valor_cita}")
        print(f"Valor atención ({tipo_atencion}): ${valor_atencion}")
        print(f"TOTAL: ${total_a_pagar}")


# ──────────────────────────────────────────────
#  FUNCIÓN: lista_clientes
#  
# ──────────────────────────────────────────────        

def mostrar_cliente():
    lista_clientes.sort(key=lambda cliente: cliente.total, reverse = True)
    print(f" {'#':<1} {'Cédula':<10}{'Nombre':<22}{'Telefono':<15}{'Tipo cliente':<15}{'Tipo atencion':<15}"
          f"{'Cant':>6} {'Prioridad':<12}{'Fecha':<11}{'Valor cita':>10}{'Valor atencion':>16}{'Total':>12}")
    for cliente in lista_clientes:
        print(f" {cliente.cedula:<12}{cliente.nombre:<22}{cliente.telefono:<15}"
              f"{cliente.tip_cliente:<15}{cliente.tip_atencion:<15}{cliente.cantidad:>6} "
              f"{cliente.prioridad:<12}{cliente.fecha:<11}{fmt_cop(cliente.valor_cita):>10}"
              f"{fmt_cop(cliente.valor_atencion):>16}{fmt_cop(cliente.total):>12}")




# ──────────────────────────────────────────────
#  FUNCIÓN: buscar_clientes
#  
# ──────────────────────────────────────────────

def buscar_cliente():
    print("Buscar cliente")
    cliente_a_buscar = input("Ingrese el numero de cedula: ")
    cliente_encontrado = None
    for cliente in lista_clientes:
        if(cliente.cedula == cliente_a_buscar):
            cliente_encontrado = cliente

    if cliente_encontrado == None:
        print("Cliente no encontrado")
    else:
        print(f" {'#':<1} {'Cédula':<10}{'Nombre':<22}{'Telefono':<15}{'Tipo cliente':<15}{'Tipo atencion':<15}"
              f"{'Cant':>6} {'Prioridad':<12}{'Fecha':<11}{'Valor cita':>10}{'Valor atencion':>16}{'Total':>12}")
        
        print(f" {cliente_encontrado.cedula:<12}{cliente_encontrado.nombre:<22}{cliente_encontrado.telefono:<15}"
            f"{cliente_encontrado.tip_cliente:<15}{cliente_encontrado.tip_atencion:<15}{cliente_encontrado.cantidad:>6} "
            f"{cliente_encontrado.prioridad:<12}{cliente_encontrado.fecha:<11}{fmt_cop(cliente_encontrado.valor_cita):>10}"
            f"{fmt_cop(cliente_encontrado.valor_atencion):>16}{fmt_cop(cliente_encontrado.total):>12}")

        
# ──────────────────────────────────────────────
#  FUNCIÓN: estadisticas
#  Main program.
# ──────────────────────────────────────────────    

def estadisticas():
    if not lista_clientes:
        print("\n  (No hay clientes registrados aún.)")
        return
    
    total_clientes = len(lista_clientes)

    ingresos_totales = 0
    for cliente in lista_clientes:
        ingresos_totales = ingresos_totales + cliente.total

    clientes_extraccion = 0
    for cliente in lista_clientes:
        clientes_extraccion = clientes_extraccion + cliente.cant_extraccion

 
    print("\n" + "═" * 50)
    print("  ESTADÍSTICAS DEL CONSULTORIO")
    print("═" * 50)
    print(f"  1. Total de clientes           : {total_clientes}")
    print(f"  2. Ingresos totales recibidos  : {fmt_cop(ingresos_totales)}")
    print(f"  3. Clientes con extracción     : {clientes_extraccion}")
    print("═" * 50)

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
        print("  2. Lista de clientes")
        print("  3. Buscar cliente")
        print("  4. Ver estadísticas")
        print("  5. Salir")
        print("─" * 50)
        opcion = input("Ingrese una oipción: ")
        if opcion == "1":
            registar_cliente()
        if opcion == "2":
            mostrar_cliente()
        if opcion == "3":
            buscar_cliente()
        if opcion == "4":
            estadisticas()
        if opcion == "5":
            ciclo_menu = False



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()