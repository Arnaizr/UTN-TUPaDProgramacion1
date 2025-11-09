#---------------------------------------------------PRÁCTICA Nº 8--------------------------------------------------#
#-------------------------------------------------MANEJO DE ARCHIVOS-----------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------Inicio del programa-----------------------------------------------------------

#Definición de funciones

#Punto 1:
# Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt 
# con tres productos. Cada línea debe tener: nombre,precio,cantidad

def crear_archivo():
    while True:
        respuesta = input("\n¡ATENCIÓN! ESTA OPCIÓN ELIMINARÁ LA BASE DE DATOS SI EL ARCHIVO YA EXISTE \n ¿Desea continuar? (Si/No): ").strip().title()
        if respuesta in ("Si", "S"): #Si la respuesta es si devuelve true para el booleano que controla el bucle
            break
        elif respuesta in ("No", "N"): #Si la respuesta es no devuelve false para el booleano que controla el bucle
            return
        else:
            print("Opción inválida, intentelo nuevamente.")
    with open(NOMBRE_ARCHIVO, "w") as primer_archivo:
        primer_archivo.write("Papel Higiénico,300,1\n")
        primer_archivo.write("Lavandina,2500,2\n")
        primer_archivo.write("Bolsa Residuos,4000,7\n")
    print(f"\nSe ha cargado el archivo {NOMBRE_ARCHIVO} con valores predeterminados.")
    return

# Punto 2:
# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: 
#           Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def impresion_productos(): #Función para imprimir variable asociada a un archivo .txt
    with open("productos.txt", "r") as primer_archivo: #Se abre el archivo como lectura
        for linea in primer_archivo: #Recorre toda las lineas del archivo 
            datos = linea.strip().split(",") #Elimina saltos de linea y separa las palabras por comas en elementos de una lista
            print(f"Producto: {datos[0]:<16} | Precio: ${datos[1]:>6} | Cantidad: {datos[2]:>2}") #Imprime con el formato solicitado
    return

# Punto 3:
# Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente


def ingreso_producto_ok(): #Verifica el que el ingreso de un nuevo producto tenga un formato válido
    booleano = False
    while not booleano: #Se mantiene dentro del bucle hasta que el usuario confirme el ingreso
        nuevo_producto = input("Por favor, ingrese el nombre del producto: ").title().strip()
        if nuevo_producto == "":
            print("\nEl producto no puede estar vacío, inténtelo nuevamente.")
            continue
        booleano = validacion() #Llama a la función de validación, si el ingreso es correcto, sale del bucle
    return nuevo_producto

def ingreso_precio():
    booleano = False
    while not booleano:
        precio = input("\nPor favor, ingrese el precio del nuevo producto: ").strip()
        if not float_ok(precio): #Si no es un flotante salta la validación y solicita un reingreso
            print("Valor incorrecto. Intentelo nuevamente") 
            continue
        if float(precio) < 0:
            print("Valor incorrecto. Intentelo nuevamente") 
            continue
        booleano = validacion()  #Llama a la función de validación, si el ingres es correcto, sale del bucle
    return(precio)

def ingreso_stock():
    booleano = False
    while not booleano:
        stock = input("\nPor favor, ingrese la cantidad del nuevo producto: ")
        if not stock.isdigit(): #Si no es un entero positivo salta la validación y solicita un reingreso
            print("Valor incorrecto. Intentelo nuevamente")
            continue
        booleano = validacion()  #Llama a la función de validación, si el ingres es correcto, sale del bucle
    return stock

def agregar_producto(nuevo_producto, precio, stock):
    nueva_linea = nuevo_producto + "," + precio + "," + stock + "\n" #Se concatenan los 3 ingresos en la primer variable
    with open(NOMBRE_ARCHIVO, "a") as primer_archivo:
        primer_archivo.write(nueva_linea)
    datos = nueva_linea.strip().split(",") #Elimina saltos de linea y separa las palabras por comas en elementos de una lista
    print(f"Se agregó: \nProducto: {datos[0]:<16} | Precio: ${datos[1]:>6} | Cantidad: {datos[2]:>2}")
    print("\nLista actualizada:\n")
    impresion_productos()
    return

# Punto 4:
# Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad

def crear_lista_de_diccionarios():
    with open(NOMBRE_ARCHIVO, "r") as variable_archivo:
        lista_de_claves = ["Nombre" , "Precio" , "Cantidad"] #Lista con los nombres de las claves de cada diccionario para cada producto
        lista_de_diccionarios = [] #Se inicializa la lista donde se almacenarán todos los productos
        for linea in variable_archivo: #Se inicia el bucle que lee cada linea de strings del archivo
            lista_de_valores = linea.strip().split(",") #Elimina saltos de linea y separa las palabras por comas en elementos de una lista
            diccionario = {} #Inicializa un diccionario donde se almacenarán los valores de cada línea
            for i in range(len(lista_de_valores)): #Recorre todos los objetos de la lista asociada a la linea actual 
                diccionario[(lista_de_claves[i])] = lista_de_valores[i] #Obtiene la clave de la lista de claves de índice "i" y le asigna la lista de valores de índice "i"  
            lista_de_diccionarios.append(diccionario) #Incorpora el diccionario creado a la lista de diccionarios
    return lista_de_diccionarios #Finalizado retorna la lista con todos los diccionarios

def impresion_lista_diccionarios(lista_diccionarios): #Función para imprimir los diccionarios de la lista
    for diccionario in lista_diccionarios: #Recorre todos los diccionarios de la lista
        cont = 0
        for key, value in diccionario.items(): #Recorre los objetos del diccionario actual e imprime claves y valores.
            cont += 1
            if key == "Precio":
                print(f"{key} : ${value}", end= "")
            else:
                print(f"{key} : {value}", end= "")
            if cont < len(diccionario):
                print(" | ", end= "")
        print("\n")

#Punto 5
# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_producto():
    nombre_producto = ingreso_producto_ok()
    if existencia_producto(nombre_producto):
        lista = crear_lista_de_diccionarios()
        for diccionario in lista:
            if diccionario["Nombre"].lower() == nombre_producto.strip().lower():
                cont = 0
                print("\n")
                for key, value in diccionario.items(): #Recorre los objetos del diccionario actual e imprime claves y valores.
                    cont += 1
                    if key == "Precio":
                        print(f"{key} : ${value}", end= "")
                    else:
                        print(f"{key} : {value}", end= "")
                    if cont < len(diccionario):
                        print(" | ", end= "")
                print("\n")
        return
    else:
        print(f"\nEl producto {nombre_producto} no se encuentra en la base de datos.")

# Punto 6
# Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.


def guardar_lista_en_archivo(lista):
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for producto in lista:
            archivo.write(f"{producto['Nombre']},{producto['Precio']},{producto['Cantidad']}\n")
    print(f"\nArchivo {NOMBRE_ARCHIVO} actualizado correctamente.")


#Funciones auxiliares

def validacion(): #Valida si se continúa en el menú o se vuelve al anterior
    while True:
        respuesta = input("\n¿El ingreso es correcto? (Si/No): ").strip().title()
        if respuesta in ("Si", "S"): #Si la respuesta es si devuelve true para el booleano que controla el bucle
            return True
        elif respuesta in ("No", "N"): #Si la respuesta es no devuelve false para el booleano que controla el bucle
            return False
        else:
            print("Opción inválida, intentelo nuevamente.")

def float_ok(flotante): #Recibe el valor de un posible flotante
    try:
        float(flotante) #Prueba de convertir el string a flotante
        return True #Si es compatible retorna true
    except ValueError: 
        return False #Si da error retorna false
    
def chequear_existencia(): #Verifica que el archivo haya sido creado 
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("\nEl archivo de productos aún no fue creado.\n")
        return False
    else:
        return True
    
def existencia_producto(nombre):
    lista = crear_lista_de_diccionarios() #Obtiene la lista de datos
    for diccionario in lista: #Recorre todos los diccionarios de la lista
        if diccionario["Nombre"].lower() == nombre.strip().lower(): #Busca un producto con igual nombre al ingresado
            return True #Si lo encuentra devuelve true
    return False #Si no lo encuentra devuelve false

def mostrar_menu():
    opcion = -1
    while opcion != "0":
        print("\n-------MENÚ-------\n")
        print("1 - Crear archivo de productos")
        print("2 - Listar productos")
        print("3 - Agregar producto")
        print("4 - Crear lista de diccionarios")
        print("5 - Buscar Producto")
        print("6 - Guardar Productos")
        print("0 - Salir")
        opcion = input("\nPor favor, ingrese una opción para continuar: ").strip()
        print("\n")

        match opcion:
            case "1":
                print("-"*20,"Crear archivo","-"*20)
                crear_archivo()
                input("\nPresione ENTER para continuar...")
            case "2":
                print("-"*20,"Listar productos","-"*20)
                print("\n")
                if chequear_existencia():
                    impresion_productos() #Llama a la función de listar el catálogo
                input("\nPresione ENTER para continuar...")                
            case "3":
                print("-"*20,"Agregar producto","-"*20)
                print("\n")
                if chequear_existencia():
                    impresion_productos()
                    print("\n")
                    nuevo_producto = ingreso_producto_ok()
                    if existencia_producto(nuevo_producto):
                        print(f"\nEl producto {nuevo_producto} ya se encuentra en la base de datos.")
                        input("\nPresione ENTER para continuar...")
                        continue
                    precio = ingreso_precio()
                    stock = ingreso_stock()
                    agregar_producto(nuevo_producto, precio, stock)
                input("\nPresione ENTER para continuar...")                
            case "4":
                print("-"*20,"Crear lista de diccionarios","-"*20)
                print("\n")
                if chequear_existencia():
                    productos = crear_lista_de_diccionarios()
                    impresion_lista_diccionarios(productos)
                input("\nPresione ENTER para continuar...")                    
            case "5":
                print("-"*20,"Buscar producto","-"*20)
                print("\n")
                if chequear_existencia():
                    buscar_producto()
                input("\nPresione ENTER para continuar...")
            case "6":
                print("-"*20,"Guardar productos actualizados","-"*20)
                print("\n")
                if chequear_existencia():
                    lista = crear_lista_de_diccionarios()
                    guardar_lista_en_archivo(lista)
                input("\nPresione ENTER para continuar...")
            case "0":
                print("-"*20,"Gracias por usar el sistema","-"*20)
                print("\n")
                continue
            case _:
                print("\nEl valor ingresado no es válido. Inténtelo nuevamente")
                input("\nPresione ENTER para continuar...")

# Programa principal

# Importación de librerías

import os

# Inicialización de variables

NOMBRE_ARCHIVO = "productos.txt"

#Llamada a la función principal del menú

mostrar_menu()