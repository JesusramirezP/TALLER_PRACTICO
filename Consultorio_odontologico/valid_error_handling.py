from datetime import datetime



def Validacion_cedula():
    el_numero_es_ok = True       
    while el_numero_es_ok ==True:     
        el_numero_tiene_error = True    
        while el_numero_tiene_error == True:
            print("Ingrese el número de cédula: ")
            dato_de_entrada = input()
            if dato_de_entrada == "":
                print("ERROR: El campo de cédula no pude ser vacío. ")
            else: 
                el_numero_tiene_error = False
            if len(dato_de_entrada) > 10:
                print("ERROR: El número de cédula no puede tener más de 10 caracteres. ")
                ciclo_try_cedu = True
            else:
                ciclo_try_cedu = False
        try:
            dato_de_entrada = int(dato_de_entrada)
            if ciclo_try_cedu == False:
                el_numero_es_ok = False
                return dato_de_entrada
        except:
            print("ERROR: Para el número de cédula por favor ingrese sólo números")



def validacion_nombre():
    el_nombre_es_ok = True    
    while el_nombre_es_ok == True:
        el_nombre_tiene_error = True    
        while el_nombre_tiene_error == True:   
            print("Ingrese nombre del cliente: ")
            nombre_del_cliente = input()
            if nombre_del_cliente == "":   
                print("ERROR: El nombre del cliente no puede ser vacio. ")
            else:
                el_nombre_tiene_error = False
            if len(nombre_del_cliente) > 22: 
                print("ERROR: El nombre del cliente no puede tener más de 22 caracteres. ")
                ciclo_try_nomb = True
            else:
                ciclo_try_nomb = False

        if not nombre_del_cliente.replace(" ", "").isalpha():   # Permitir espacios
            print("ERROR: Para el nombre del cliente por favor ingrese sólo letras.")
        else:
            if ciclo_try_nomb == False:
                el_nombre_es_ok = False
                return nombre_del_cliente
            

def Validacion_telef():
    el_numero_es_ok = True       
    while el_numero_es_ok ==True:     
        el_numero_tiene_error = True    
        while el_numero_tiene_error == True:
            print("Ingrese número de teléfono: ")
            dato_de_entrada = input()
            if dato_de_entrada == "":
                print("ERROR: El campo de telefono no pude ser vacío. ")
            else: 
                el_numero_tiene_error = False
            if len(dato_de_entrada) > 15:
                print("ERROR: El número de telefono no puede tener más de 15 caracteres. ")
                ciclo_try_tel = True
            else:
                ciclo_try_tel = False
        try:
            dato_de_entrada = int(dato_de_entrada)
            if ciclo_try_tel == False:
                el_numero_es_ok = False
                return dato_de_entrada
        except:
            print("ERROR: Para el número de telefono por favor ingrese sólo números")




def validar_fecha():
    while True:
        print("Ingrese fecha de la cita (DD/MM/AAAA): ")
        fecha = input()
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("ERROR: Fecha inválida. Use DD/MM/AAAA")          
            
