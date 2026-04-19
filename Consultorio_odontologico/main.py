"""
Aplicación para consultorio odontologico.
Version v1.

Que incluye;
    - Variables
        - input
        - output
        - Tipos de variables:
            - String (str) cadena de texto o cadena de caracteres.
            - Numericas (int): 
            - Boolean (bool): True or False
            - Objeto: Tipos personalizados
            - lista
            - Diccionario
    - Operadores
        - + : suma
    - Modulos
    - Funciones

Problemas (BUGS) que se encontraron y se corrigieron.
    1. Valida que el numero de cedula no sea vacío.
    2. Valida que el numero de cedula sea numérico.     "Manejo de errores"
    3. Valida que el numero de cedula no tenga mas de 10 caracteres.

    4. Valida que el nombre del cliente no sea vacío.
    5. Valida que el nombre del cliente solo tenga letras.
    6. Valida que el numbre del cliente no tenga mas de 22 caracteres.

    7. Valida que el numero de telefono no sea vacío.
    8. Valida que el numero de telefono sea numérico.   "Manejo de errores"
    9. Valida que el numero de telefono no tenga mas de 15 caracteres.

    10. Valida que la fecha de la cita no este vacia.
    11. Valida que la fecha de la cita tenga el formato DD/MM/AAAA.  "Manejo de errores"
    12. "Manejo de errores"alida que la fecha tenga valores exagerados en dia y mes.     "Manejo de errores"

    13. Valida que al ingresar las opciones al menu no esten vacias y concuerden con la longitud del menu.
    14. Valida que sean numeros dentro de la longitud del menu.

    15. Valida que la cantidad de calzas y extracciones no sea vacia.
    16. Valida que la cantidad de calzas y extraciones no supere las 32 piezas dentales.
    17. valida que el numero de calzas y extracciones sea numerico. "Manejo de errores"

"""


from typing import List
from cliente import Cliente
from tarifas import TARIFAS
from valid_error_handling import Validacion_cedula, validacion_nombre, Validacion_telef, validar_fecha, validar_opcion_menu, cant_intervenciones



# lista = arreglo = colección
lista_clientes: list[Cliente] = [ ]


# ──────────────────────────────────────────────
#  FUNCIÓN: Formato para moneda colombiana.
# ──────────────────────────────────────────────

def fmt_cop(valor: int) -> str:      
    return f"${valor:,.0f}".replace(",", ".")

# ──────────────────────────────────────────────
#  FUNCIÓN: Registar cliente    "1"
# ──────────────────────────────────────────────
def registar_cliente():
    print("\n")                     #Solo información en terminal                        
    print("  NUEVO CLIENTE.")       #Solo información en terminal 
    
    print("\n" + "─" * 50)              #Solo información en terminal
    print("  Datos personales.")        #Solo información en terminal 
    print("─" * 50)                     #Solo información en terminal 

    cedula_cliente = Validacion_cedula()    #Se realiza proceso de captura y validación para el numero de cédula en el modulo "valid_error_handling.py"
    nombre_cliente = validacion_nombre()    #Se realiza proceso de captura y validación para el nombre en el modulo "valid_error_handling.py"
    telefono_cliente = Validacion_telef()   #Se realiza proceso de captura y validación para el numero de telefono en el modulo "valid_error_handling.py"

    print("\n" + "─" * 50)              #Solo información en terminal 
    print("  Tipo de cliente.")         #Solo información en terminal 
    print("─" * 50)                     #Solo información en terminal 

    print("  1. Particular")    #Solo información en terminal 
    print("  2. EPS")           #Solo información en terminal 
    print("  3. Prepagada")     #Solo información en terminal 
    
    tipo_cliente = validar_opcion_menu(["1","2","3"])   #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if tipo_cliente == "1":
        tipo_cliente = "Particular"     #Guarda dato en varible dependiendo del valor de la opcion
    if tipo_cliente == "2":
        tipo_cliente = "EPS"            #Guarda dato en varible dependiendo del valor de la opcion
    if tipo_cliente == "3":
        tipo_cliente = "Prepagada"      #Guarda dato en varible dependiendo del valor de la opcion

    print("\n" + "─" * 50)              #Solo información en terminal
    print("  Tipo de atención.")        #Solo información en terminal
    print("─" * 50)                     #Solo información en terminal

    print("  1. Limpieza")              #Solo información en terminal
    print("  2. Calzas")                #Solo información en terminal
    print("  3. Extracción")            #Solo información en terminal
    print("  4. Diagnostico")           #Solo información en terminal

    cant_procedimientos = 0             #Se inicializan variables
    numero_extracciones = 0             #Se inicializan variables

    tipo_atencion = validar_opcion_menu(["1","2","3","4"])  #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if tipo_atencion == "1":
        tipo_atencion = "Limpieza"      #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = 1         #Guarda dato en varible para que limpieza siempre sea 1

    if tipo_atencion == "2":            
        tipo_atencion = "Calzas"         #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = cant_intervenciones("calzas")     #Se realiza proceso de captura del numero de calzas en el modulo "valid_error_handling.py", se reutiliza funcion "cant_intervenciones"

    if tipo_atencion == "3":
        tipo_atencion = "Extracción"                                #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = cant_intervenciones("extracciones")   #Se realiza proceso de captura del numero de calzas en el modulo "valid_error_handling.py", se reutiliza funcion "cant_intervenciones"
        numero_extracciones = cant_procedimientos                   #Guarda dato en varible auxiliar

    if tipo_atencion == "4":
        tipo_atencion = "Diagnóstico"       #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = 1                 #Guarda dato en varible para que siempre sea 1 *******

    print("\n" + "─" * 50)                  #Solo información en terminal
    print("  Prioridad de atención.")       #Solo información en terminal
    print("─" * 50)                         #Solo información en terminal
    
    print("  1. Normal")                    #Solo información en terminal
    print("  2. Urgente")                   #Solo información en terminal
    prioridad_atencion = validar_opcion_menu(["1","2"])     #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if prioridad_atencion == "1":
        prioridad_atencion = "Normal"       #Guarda dato en varible dependiendo del valor de la opcion
    if prioridad_atencion == "2":           
        prioridad_atencion = "Urgente"      #Guarda dato en varible dependiendo del valor de la opcion

    print("\n" + "─" * 50)                  #Solo información en terminal
    print("  Fecha para la cita.")          #Solo información en terminal
    print("─" * 50)                         #Solo información en terminal

    fecha_cita = validar_fecha()   #Se realiza proceso de captura de la fecha en el modulo "valid_error_handling.py", en la funcion "validar_fecha"

    valor_cita = TARIFAS[tipo_cliente]["cita"]              #Consulta diccionario para los datosd precios de los diferentes servicios, en el modulo "tarifas.py"
    valor_atencion = TARIFAS[tipo_cliente][tipo_atencion]   #Consulta diccionario para los datosd precios de los diferentes servicios, en el modulo "tarifas.py"
    valor_atencion = valor_atencion * cant_procedimientos   #Calculo del valor de la atención programada
    total_a_pagar = valor_cita + valor_atencion             #Calculo del valor total para el usuario registrado

    cliente = Cliente()                                     #Se crea un cliente
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

    print("\n" + "─" * 50)              #Solo información en terminal
    print("  RESUMEN DE PAGO.")         #Solo información en terminal
    print("─" * 50)                     #Solo información en terminal
    
    print(f"{'1. Valor cita':<35}: {fmt_cop(valor_cita):>10}")                              #Solo información en terminal de forma tabulada
    print(f"{f'2. Valor atención ({tipo_atencion})':<35}: {fmt_cop(valor_atencion):>10}")   #Solo información en terminal de forma tabulada
    print(f"{'3. TOTAL':<35}: {fmt_cop(total_a_pagar):>10}")                                #Solo información en terminal de forma tabulada


# ──────────────────────────────────────────────
#  FUNCIÓN: Lista clientes  "2"
# ──────────────────────────────────────────────        
def mostrar_cliente():                          #Solo información en terminal
    print("\n" + "─" * 50)                      #Solo información en terminal
    print("  Lista de clientes.")               #Solo información en terminal
    print("─" * 50)
    lista_clientes.sort(key=lambda cliente: cliente.total, reverse = True)          #Se ordena los clientes de mayor a menor de acuerdo al precio total
    print(f" {'#':<1} {'Cédula':<10}{'Nombre':<22}{'Telefono':<15}{'Tipo cliente':<15}{'Tipo atencion':<15}"    #Imprime encabezado de la tabla de clientes
          f"{'Cant':>6} {'Prioridad':<12}{'Fecha':<11}{'Valor cita':>10}{'Valor atencion':>16}{'Total':>12}")   #Imprime encabezado de la tabla de clientes
    for cliente in lista_clientes:                                                                  #Ciclo for para imprimir los clientes en el terminal
        print(f" {cliente.cedula:<12}{cliente.nombre:<22}{cliente.telefono:<15}"                    #Imprime los clientes de forma ordenada
              f"{cliente.tip_cliente:<15}{cliente.tip_atencion:<15}{cliente.cantidad:>6} "          #
              f"{cliente.prioridad:<12}{cliente.fecha:<11}{fmt_cop(cliente.valor_cita):>10}"        #
              f"{fmt_cop(cliente.valor_atencion):>16}{fmt_cop(cliente.total):>12}")                 #


# ──────────────────────────────────────────────
#  FUNCIÓN: Buscar_clientes     "3"
# ──────────────────────────────────────────────
def buscar_cliente():               #Solo información en terminal
    print("\n" + "─" * 50)          #Solo información en terminal
    print("  Buscar cliente.")      #Solo información en terminal
    print("─" * 50)                 #Solo información en terminal
    
    cliente_a_buscar = Validacion_cedula()      #Se realiza proceso de captura y validación para el numero de cédula en el modulo "valid_error_handling.py"
    cliente_encontrado = None                   #Se inicializa variable
    for cliente in lista_clientes:              #Ciclo for para buscar el cliente
        if(cliente.cedula == cliente_a_buscar):
            cliente_encontrado = cliente

    if cliente_encontrado == None:              #Cliente no encontrado
        print("Cliente no encontrado")
    else:
        print(f" {'#':<1} {'Cédula':<10}{'Nombre':<22}{'Telefono':<15}{'Tipo cliente':<15}{'Tipo atencion':<15}"        #Imprime encabezado de la tabla para mostrar cliente
              f"{'Cant':>6} {'Prioridad':<12}{'Fecha':<11}{'Valor cita':>10}{'Valor atencion':>16}{'Total':>12}")       #Imprime encabezado de la tabla para mostrar cliente
        
        print(f" {cliente_encontrado.cedula:<12}{cliente_encontrado.nombre:<22}{cliente_encontrado.telefono:<15}"               #Imprime los clientes de forma ordenada
            f"{cliente_encontrado.tip_cliente:<15}{cliente_encontrado.tip_atencion:<15}{cliente_encontrado.cantidad:>6} "       #
            f"{cliente_encontrado.prioridad:<12}{cliente_encontrado.fecha:<11}{fmt_cop(cliente_encontrado.valor_cita):>10}"     #
            f"{fmt_cop(cliente_encontrado.valor_atencion):>16}{fmt_cop(cliente_encontrado.total):>12}")                         #

        
# ──────────────────────────────────────────────
#  FUNCIÓN: Ver estadisticas    "4"
# ──────────────────────────────────────────────    
def estadisticas():
    if not lista_clientes:                                  #Consulta si la lista no esta vacia
        print("\n  (No hay clientes registrados aún.)")
        return                                              #Si la lista esta vacia retorna al menu principal
    
    total_clientes = len(lista_clientes)        #Guarda el numero de clientes que tiene la lista

    ingresos_totales = 0                        #Inicializa variable para calcular los ingresos totales
    for cliente in lista_clientes:              #Ciclo for para calcular los ingresos totales
        ingresos_totales = ingresos_totales + cliente.total     #Calculo para los ingresos totales

    clientes_extraccion = 0                     #Inicializa variable para el conteo de clientes con extracciones
    for cliente in lista_clientes:              #Ciclo for para calcular el numero de clientes para extracción
        if cliente.cant_extraccion > 0:         #Verifica que cant_extraccion no este vacio
            clientes_extraccion = clientes_extraccion + 1   #Suma todos los clientes con extracción

    print("\n" + "═" * 50)                      #Solo información en terminal
    print("  ESTADÍSTICAS DEL CONSULTORIO")     #Solo información en terminal       
    print("═" * 50)                             #Solo información en terminal
    print(f"  1. Total de clientes           : {total_clientes}")               #Imprime en el terminal el total de clientes
    print(f"  2. Ingresos totales recibidos  : {fmt_cop(ingresos_totales)}")    #Imprime en el terminal el total de ingresos
    print(f"  3. Clientes con extracción     : {clientes_extraccion}")          #Imprime en el terminal el número de persona para extracción
    print("═" * 50)


# ──────────────────────────────────────────────
#  FUNCIÓN: menu
# ──────────────────────────────────────────────
def menu():
    ciclo_menu = True                                       
    while ciclo_menu == True:                               #Solo información en terminal
        print("\n" + "═" * 50)                              #Solo información en terminal
        print("  CONSULTORIO ODONTOLÓGICO — Dr. AAA")       #Solo información en terminal
        print("═" * 50)                                     #Solo información en terminal
        print("  1. Registrar nuevo cliente")               #Solo información en terminal
        print("  2. Lista de clientes")                     #Solo información en terminal
        print("  3. Buscar cliente")                        #Solo información en terminal
        print("  4. Ver estadísticas")                      #Solo información en terminal
        print("  5. Salir")                                 #Solo información en terminal
        print("─" * 50)                                     #Solo información en terminal
        opcion = input("Ingrese una oipción: ")             #Captura dato para seleccionar la opcion a trabajar
        if opcion == "1":
            registar_cliente()
        if opcion == "2":
            mostrar_cliente()
        if opcion == "3":
            buscar_cliente()
        if opcion == "4":
            estadisticas()
        if opcion == "5":
            ciclo_menu = False                            #Fin del programa



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()