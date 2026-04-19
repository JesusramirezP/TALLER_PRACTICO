from datetime import datetime



def Validacion_cedula():
    el_numero_es_ok = True       
    while el_numero_es_ok ==True:     
        el_numero_tiene_error = True    
        while el_numero_tiene_error == True:
            #print("Ingrese el número de cédula: ")
            dato_de_entrada = input("Ingrese el número de cédula: ")
            if dato_de_entrada == "":
                print("ERROR: El campo de cédula no pude estar vacío. ")
            else: 
                el_numero_tiene_error = False
            if len(dato_de_entrada) > 10:
                print("ERROR: El número de cédula no puede tener más de 10 caracteres. ")
                ciclo_try_cedu = True
            else:
                ciclo_try_cedu = False
        try:
            if not dato_de_entrada.isdigit():
                print("ERROR: Para el número de cédula, ingrese solo números.")
                continue
            dato_de_entrada = int(dato_de_entrada)

            if dato_de_entrada <= 0:
                print("ERROR: El número de cedula debe de ser un número positivo.")
                el_numero_es_ok = True
                continue

            if ciclo_try_cedu == False:
                el_numero_es_ok = False
                return dato_de_entrada
        except:
            print("ERROR: Para el número de cédula, ingrese solo números.")



def validacion_nombre():
    el_nombre_es_ok = True    
    while el_nombre_es_ok == True:
        el_nombre_tiene_error = True    
        while el_nombre_tiene_error == True:   
            #print("Ingrese nombre del cliente: ")
            nombre_del_cliente = input("Ingrese nombre del cliente: ")
            if nombre_del_cliente == "":   
                print("ERROR: El campo de nombre del cliente no puede estar vacío.")
            else:
                el_nombre_tiene_error = False
            if len(nombre_del_cliente) > 22: 
                print("ERROR: El nombre del cliente no puede tener más de 22 caracteres. ")
                ciclo_try_nomb = True
            else:
                ciclo_try_nomb = False

        if not nombre_del_cliente.replace(" ", "").isalpha():   # Permitir espacios
            print("ERROR: Para el nombre del cliente, ingrese solo letras.")
        else:
            if ciclo_try_nomb == False:
                el_nombre_es_ok = False
                return nombre_del_cliente
            

def Validacion_telef():
    el_numero_es_ok = True       
    while el_numero_es_ok ==True:     
        el_numero_tiene_error = True    
        while el_numero_tiene_error == True:
            #print("Ingrese número de teléfono: ")
            dato_de_entrada = input("Ingrese número de teléfono: ")
            if dato_de_entrada == "":
                print("ERROR: El campo de teléfono no puede estar vacío.")
            else: 
                el_numero_tiene_error = False
            if len(dato_de_entrada) > 15:
                print("ERROR: El número de telefono no puede tener más de 15 caracteres. ")
                ciclo_try_tel = True
            else:
                ciclo_try_tel = False
        try:
            if not dato_de_entrada.isdigit():
                print("ERROR: Para el número de telefono, ingrese solo números.")
                continue
            dato_de_entrada = int(dato_de_entrada)

            if dato_de_entrada <= 0:
                print("ERROR: El número de cedula debe de ser un número positivo.")
                el_numero_es_ok = True
                continue
            
            if ciclo_try_tel == False:
                el_numero_es_ok = False
                return dato_de_entrada
        except:
            print("ERROR: Para el número de teléfono, ingrese solo números.")




def validar_fecha():
    while True:
        #print("Ingrese fecha de la cita (DD/MM/AAAA): ")
        fecha = input("Ingrese fecha de la cita (DD/MM/AAAA): ")
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("ERROR: Fecha inválida. Use DD/MM/AAAA")     


def validar_opcion_menu(opciones_validas):
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in opciones_validas:
            return opcion
        print("Opción inválida")


def cant_intervenciones(mensaje):
    while True:
        entrada = input(f"Ingrese cantidad de {mensaje} >0: ").strip()
        if entrada == "":
            print("Debe ingresar un valor")
            continue

        try:
            valor = int(entrada)
        except ValueError:
            print("ERROR: Solo se permiten números enteros")
            continue

        if valor < 0:
            print(f"ERROR: El número ingresado no es valido")
            continue

        if valor > 32:
            print(f"ERROR: El número ingresado supera las 32 piezas dentales")
            continue

        return valor


                
            
