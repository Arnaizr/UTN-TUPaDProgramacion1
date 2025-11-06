#---------------------------------------------------PRÁCTICA Nº 7--------------------------------------------------#
#--------------------------------------------------DATOS COMPLEJOS-------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


#Ejercicio N° 1
# Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 1---------------------------\n")

#Definición de funciones

def impresion_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key} : {value}", end=" | ")    
    return None

#--------Programa principal--------

# Declaración del diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Incorporación de las nuevas frutas y precios
precios_frutas.update({'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300})

#Muestra del diccionario actualizado
impresion_diccionario(precios_frutas)

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 1-----------------------\n")



#Ejercicio N° 2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 2---------------------------\n")

#Definición de funciones

def impresion_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key} : {value}", end=" | ")    
    return None

#--------Programa principal--------

#Actualización de los precios de las frutas seleccionadas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Muestra del diccionario actualizado
impresion_diccionario(precios_frutas)

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 2-----------------------\n")

#Ejercicio N° 3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 3---------------------------\n")

#Definición de funciones

def impresion_lista(lista):
    for valor in lista:
        print(valor, end=" | ")
    return None    

#--------Programa principal--------

#Se extraen las keys del diccionario, se las convierte a lista y se las almacena en una nueva variable
lista_frutas = list(precios_frutas.keys())

#Salida de datos
impresion_lista(lista_frutas)

#--------Fin del programa--------
print("\n\n-----------------------Fin del Ejercicio Nº 3-----------------------\n")


#Ejercicio N° 4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 4---------------------------\n")

#Definición de funciones

def telefono_valido(numero):
    if numero.isdigit(): #Se verifica que la cantidad sea un entero válido (no admite negativos ni flotantes)
        if 6 < len(numero) < 15: #Se verifica que sea de una longitud adecuada
            return numero #Se devuelve el número convertido
        else:
            return False #Si no cumple se devuelve falso
    else:
        return False #Si no cumple se devuelve falso

def impresion_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"- {key} : {value}")    
    return None

#--------Programa principal-------
#Inicialización de variables
contactos = {} #Inicializa el diccionario
i = 0 #Inicializa variable de control del bucle

#Inicio de bucle para cargar contactos
while i < 5:
    nombre = input(f"\nPor favor, ingrese el nombre del {i+1}º contacto para agregar: ").title()
    telefono = input(f"Por favor, ingrese el número de teléfono de {nombre}: ")
    telefono = telefono_valido(telefono) #Se llama a la función que verifica el número de teléfono
    if telefono != False: #Si la función de número de teléfono no dio falsa se chequea el nombre
        if nombre in contactos: #Si el contacto ya está en la agenda se solicita uno nuevo
            print(f"{nombre} ya está agendado, ingresá otro contacto.")
        else:
            contactos[nombre] = telefono #Se agenda el nuevo contacto y teléfono
            i += 1 #Se incrementa la variable de control del bucle
    else:
        print("El número ingresado no fue válido. Intentalo nuevamente.")
#Fin del bucle

#Muestra de la agenda completa
print("\nLista de contactos:")
impresion_diccionario(contactos)

#Inicio de bucle que devuelve el número de teléfono de los contactos hasta que se salga.

while True:
    nombre = input(f"\nPor favor, ingrese el nombre de un contacto: ").title()
    if nombre in contactos: #Si el contacto está en la agenda se muestra el teléfono
        print(f"El teléfono de {nombre} es: {contactos[nombre]}.")
    else:
        print(f"{nombre} no está agendado.")
    while True:
        seguir = input("\n¿Desea ver otro número? (S/N): ").capitalize()
        if seguir == "S":
            salir = False
            break
        elif seguir == "N":
            salir = True
            break
        else:
            print("Valor incorrecto. Ingrese S o N.")
    if salir:
        break

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 4-----------------------\n")

#Ejercicio N° 5
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 5---------------------------\n")

#Definición de funciones

def impresion_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key} : {value}", end=" | ")    
    return None

def impresion_lista(lista):
    for valor in lista:
        print(valor, end=" | ")
    return None    

#Programa principal
#Inicialización de variables

diccionario_frase = {} #Se inicializa el diccionario donde se almacenan las palabras de la frase y sus repeticiones

#Solicitud de ingreso de variables

frase = input("Por favor, ingrese una frase para su recuento: ")

#Oparaciones

lista_frase = frase.split() #Se convierte el string ingresado a una lista para su uso
palabras_unicas = set(lista_frase) #Se convierte la lista a un set para agrupar valores repetidos


for i in palabras_unicas: #Repasa todo el conjunto de a un valor
    repeticion_valores = lista_frase.count(i) #Cuenta cuántas veces se repite el valor actual en la lista
    diccionario_frase[i] = repeticion_valores #Se agrega el valor actual al diccionario como llave junto con la cantidad de veces que aparece como value

print(f"La frase ingresada es: {frase}\n")
print(f"Las palabras utilizadas sin repetir son: ")
impresion_lista(palabras_unicas)
print(f"\n\nLa cantidad de veces que apareció cada palabra es: ") 
impresion_diccionario(diccionario_frase)

#--------Fin del programa--------
print("\n\n-----------------------Fin del Ejercicio Nº 5-----------------------\n")



#Ejercicio N° 6
#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 6---------------------------\n")

#Definición de funciones

def promedio_tupla(tupla):
    sumatoria = 0
    for numero in tupla:
        sumatoria += numero
    promedio = round(sumatoria/len(tupla), 2)
    return promedio

def nota_ok(nota): #Recibe el valor de un posible flotante
    try:
        float(nota) #Prueba de convertir el string a flotante
        return True #Si es compatible retorna true
    except ValueError: 
        return False #Si da error retorna false
        
#Programa principal

#Inicialización de variables
alumnos = {}
ingresar = "Si"
contador = 0
while ingresar in ("Si" ,"S"):
    alumno_ingreso = input(f"\nPor favor, ingrese el nombre del {contador+1}° alumno: ").title()
    if alumno_ingreso not in alumnos:
        notas = []
        for i in range (3):
            while True:
                nota_actual = input(f"Por favor, ingrese la {i+1}° nota de {alumno_ingreso}: ")
                if nota_ok(nota_actual):
                    nota_actual = float(nota_actual)
                    if 0 <= nota_actual <= 10:
                        break
                    else:
                        print(f"{nota_actual} no está en el rango correcto. Ingrese nuevamente.")
                else:
                    print(f"{nota_actual} no es un valor numérico. Ingrese nuevamente.")
            notas.append(nota_actual)
        alumnos[alumno_ingreso] = tuple(notas)
        contador += 1
    else:
        print(f"{alumno_ingreso} ya se encuentra en la base de datos, intente con otro nombre")
    while True:
        ingresar = input(f"¿Desea ingresar un nuevo alumno? (Si/No): ").title()
        if ingresar == "Si" or ingresar == "S":
            break
        elif ingresar == "No" or ingresar == "N":
            break
        else:
            print("Valor incorrecto. Intente nuevamente.")
    
    #Salida de resultados
    
for key, value in alumnos.items():
    print(f"\nEl promedio del alumno {key} es: {promedio_tupla(value)}.")
    
#--------Fin del programa--------
print("\n\n-----------------------Fin del Ejercicio Nº 6-----------------------\n")



#Ejercicio N° 7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 7---------------------------\n")


# #-----------Como alternativa se creó esta función aleatoria que genera números de ID aleatorios para llenar los sets---------------
# #Importación de función aleatoria
# import random
# #Se inicializan los 2 set de aprobados de cada materia
# aprobados_parcial_1 = set() 
# aprobados_parcial_2 = set()
# #Se inicializa un bucle para cargar los dos sets con números de ID aleatorios de los alumnos 
# for i in range (2):
#     cont = 0 #Se inicializa un contador para cargar los dos sets
#     while cont < 20: #se genera un bucle que carga cada set con al menos 20 alumnos que aprobaron el parcial
#         ID = str(random.randint(1 , 100)) #Se genera un número aleatorio de ID
#         while len(ID) < 3:
#             ID = "0" + ID #En el caso que el número aleatorio sea menor a 3 dígitos se agrega un 0 a la izquierda
#         if i == 0:    #Control para agregar los valores al primer set según las repeticiones, si no se agrega al otro
#             if ID not in aprobados_parcial_1:
#                 aprobados_parcial_1.add(ID)
#                 cont += 1
#         else:
#             if ID not in aprobados_parcial_2:
#                 aprobados_parcial_2.add(ID)
#                 cont += 1
# #----------------------------------------------------------------------------------------------------------------------------------

# Programa Principal

#Se inicializan los dos sets con ID aleatorios de alumnos
aprobados_parcial_1 = {'026', '001', '073', '056', '066', '008', '031', '040', '097', '044', '053', '027', '098', '043', '094', '009', '039', '013', '093', '074'}
aprobados_parcial_2 = {'037', '052', '072', '068', '016', '088', '040', '087', '011', '047', '062', '081', '098', '044', '083', '035', '071', '086', '013', '074'}

# #Como alternativa se inicializan dos sets con nombres y apellidos
# aprobados_parcial_1 = {'Pablo Garcia', 'Luis Perez', 'Martin Garcia', 'Luis Garcia', 'Karina Perez', 'Rodrigo Garcia', 'Rodrigo Perez', 'Luisa Garcia', 'Luisa Perez', 'Sofia Perez', 'Luis Gonzalez', 'Pablo Gonzalez', 'Pablo Gomez', 'Juan Garcia', 'Juan Perez', 'Felipe Perez', 'Felisa Perez', 'Martina Garcia', 'Martina Perez', 'Felisa Garcia'}
# aprobados_parcial_2 = {'Pamela Garcia', 'Pamela Flores', 'Sofia Flores', 'Karina Flores', 'Pablo Flores', 'Pedro Flores', 'Martin Flores', 'Luis Flores', 'Santiago Garcia', 'Santiago Gonzalez', 'Santiago Perez', 'Sebastian Perez', 'Sebastian Garcia', 'Rodrigo Gonzalez', 'Luis Garcia', 'Federico Garcia', 'Karina Garcia', 'Karina Perez', 'Rodrigo Perez', 'Sofia Perez'}


print("\nAlumnos que aprobaron el parcial 1: ", sorted(aprobados_parcial_1))
print("\nAlumnos que aprobaron el parcial 2: ", sorted(aprobados_parcial_2))

print("\n--------RESULTADOS-------\n")

print("\nAlumnos que aprobaron sólo el parcial 1: ", sorted(aprobados_parcial_1 - aprobados_parcial_2))
print("\nAlumnos que aprobaron sólo el parcial 2: ", sorted(aprobados_parcial_2 - aprobados_parcial_1))
print("\nAlumnos que aprobaron ambos parciales: ", sorted(aprobados_parcial_1 & aprobados_parcial_2))
print("\nAlumnos que aprobaron al menos un parcial: ", sorted(aprobados_parcial_1 | aprobados_parcial_2))

#--------Fin del programa--------
print("\n\n-----------------------Fin del Ejercicio Nº 7-----------------------\n")



#Ejercicio Nº 8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 8---------------------------\n")

#Definición de funciones

def float_ok(flotante): #Recibe el valor de un posible flotante
    try:
        float(flotante) #Prueba de convertir el string a flotante
        return True #Si es compatible retorna true
    except ValueError: 
        return False #Si da error retorna false

def validacion(): #Valida si se continúa en el menú o se vuelve al anterior
    while True:
        respuesta = input("\n¿Desea realizar otra operación en este menú? (Si/No): ").strip().title()
        if respuesta in ("Si", "S"): #Si la respuesta es si devuelve true para el booleano que controla el bucle
            return True
        elif respuesta in ("No", "N"): #Si la respuesta es no devuelve false para el booleano que controla el bucle
            return False
        else:
            print("Opción inválida, intentelo nuevamente.")

def impresion_diccionario(diccionario): #Función de impresión del diccionario para mostrar el catálogo de productos
    for key, value in diccionario.items():
        print(f"- {key} : {value}")    
    return None

#Programa principal

#Inicialización de variables
productos = {"Papel higiénico" : 20, "Polenta" : 24, "Fideos" : 44, "Lavandina" : 15, "Tomate" : 24.5} #Se inicializa el diccionario con valores de productos y stock predeterminados
opcion = -1 #Se inicializa la variable de control de menú para que ingrese al bucle
while opcion != 0:
    print("\n-------MENÚ-------\n")
    print("1 - Consultar stock")
    print("2 - Agregar unidades")
    print("3 - Agregar al catálogo")
    print("4 - Mostrar catálogo")
    print("0 - Salir")
    
    opcion = input("\nPor favor, ingrese una opción para continuar: ")

    try:
        opcion = int(opcion)
    except ValueError:
        opcion = -1

    match opcion:
        case 1:
            booleana = True #Se inicializa la variable control del bucle de la opción 1
            while booleana: #Se repite el bucle hasta que el usuario decida volver al menú anterior
                prod_actual = input("Por favor, ingrese un producto para consultar su stock: ").strip().title()  
                if productos.get(prod_actual) is None: #Si el producto no está cargado como clave en el diccionario se informa al usuario
                    print(f"- {prod_actual} - no existe en la base de datos, inténtelo nuevamente.")
                else:
                    print(f"El stock de - {prod_actual} - es: {productos[prod_actual]}.") #Si el producto está en el diccionario se informa el stock
                booleana = validacion() #Se llama a la función para volver al menú anterior o realizar otra consulta
        case 2:
            booleana = True #Se inicializa la variable control del bucle de la opción 2
            while booleana: #Se repite el bucle hasta que el usuario decida volver al menú anterior
                prod_actual = input("Por favor, ingrese un producto para agregar stock: ").strip().title()
                if prod_actual.strip() == "": #Se corrobora que el usuario no haya ingresado espacios en blanco
                    print("\nDebe ingresar un valor para continuar, inténtelo nuevamente.")
                elif productos.get(prod_actual) is None: #Si el producto no está cargado como clave en el diccionario se informa al usuario
                    print(f"- {prod_actual} - no existe en la base de datos, inténtelo nuevamente.")
                else: #Si el producto está en el diccionario se procede a ingresar el stock
                    booleana2 = True #Se inicializa la variable de control del segundo bucle
                    while booleana2: #Se repite el buclle hasta que el usuario ingrese una cantidad válida para el producto
                        act_stock = input(f"Por favor, ingrese cuánto stock de - {prod_actual} - desea agregar: ")
                        if float_ok(act_stock): #Se llama a la función que corrobora si el valor ingresado es un flotante válido
                            act_stock = round(float(act_stock), 2) #Si es válido se convierte a flotante
                            if act_stock >= 0: 
                                productos[prod_actual] += act_stock #Si es mayor o igual a cero se informa al usuario
                                print(f"\nEl stock de - {prod_actual} - ahora es {productos[prod_actual]}.\n")
                                booleana2 = False #Se cambia el valor de la variable booleana para salir del bucle
                            else:
                                print(f"\n{act_stock} no es una cantidad válida, por favor intentelo nuevamente.")     
                        else:
                            print(f"\n{act_stock} no es una cantidad válida, por favor intentelo nuevamente.")
                booleana = validacion() #Se llama a la función para volver al menú anterior o realizar otra operación
        case 3:
            booleana = True #Se inicializa la variable control del bucle de la opcion 3
            while booleana: #Se repite el bucle hasta que el usuario decida volver al menú anterior
                prod_actual = input("Por favor, ingrese un producto para agregar al catálogo: ").strip().title()
                if productos.get(prod_actual) is not None: #Si el producto se encuentra en el diccionario se solicita otro valor
                        print(f"- {prod_actual} - ya existe en la base de datos, inténtelo nuevamente.")
                elif prod_actual.strip() == "": #Se vverifica que el usuario no ingrese espacios en blanco como producto
                    print("\nDebe ingresar un valor para continuar, inténtelo nuevamente.")
                else: #Si el producto no está cargado como clave se procede al ingreso
                    booleana2 = True #Se inicializa la variable del segundo bucle
                    while booleana2: #Se repite el bucle hasta que el usuarioo ingrese una cantidad válida para el producto
                        stock_ini = input(f"Por favor, ingrese cuánto stock inicial de {prod_actual} se ingresa: ")
                        if float_ok(stock_ini): #Se llama a la función que corrobora que el valor sea un flotante válido
                            stock_ini = round(float(stock_ini), 2) #En caso afirmativo se convierte a flotante 
                            if stock_ini >= 0: #Se verifica que no se ingresen cantidades negativas
                                productos[prod_actual] = stock_ini
                                print(f"\nSe ha agregado el producto - {prod_actual} - con un stock de {productos[prod_actual]} unidades.\n")
                                booleana2 = False #Se cambia el valor de la variable para salir del bucle
                            else:
                                print(f"\n{stock_ini} no es una cantidad válida, por favor intentelo nuevamente.")
    
                        else:
                            print(f"\n{stock_ini} no es una cantidad válida, por favor intentelo nuevamente.")
                booleana = validacion() #Se llama a la función para verificar si se desea realizar otra operación o volver al menú anterior
        case 4:
            print("\nCatálogo:\n")
            impresion_diccionario(productos) #Se imprime el catálogo para ver el estado del diccionario
            input("Presione ENTER para continuar")
        case 0:
            print("\nGracias por usar el sistema")
        case _:
            print("Opción inválida, por favor inténtelo nuevamente.")
            input("Presione ENTER para continuar")
    
print("\n\n-------------Fin del ejercicio n° 8---------------\n")


#Ejercicio Nº 9
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
# Ejemplo:
# agenda = {
#     ("lunes", "10:00") : "Reunión" 
#     ("martes", "15:00") : "Clase de inglés" 
# }
# Permití consultar qué actividad hay en cierto día y hora.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 9---------------------------\n")

#Definición de funciones

def validacion(): #Valida si se continúa en el menú o se vuelve al anterior
    while True:
        respuesta = input("\n¿Desea continuar? (Si/No): ").strip().title()
        if respuesta in ("Si", "S"): #Si la respuesta es si devuelve true para el booleano que controla el bucle
            return True
        elif respuesta in ("No", "N"): #Si la respuesta es no devuelve false para el booleano que controla el bucle
            return False
        else:
            print("Opción inválida, intentelo nuevamente.")

def check_horario(HH, MM): #Función para verificar el formato de la hora
    try: #Se verifica que horas y minutos sean enteros
        HH = int(HH) 
        MM = int(MM)
    except ValueError: #Caso contrario se retorna falso
        return False
    if 0 <= HH <= 23 and 0 <= MM <= 59: #Se verifica que estén en el rango correcto
        return f"{HH:02d}:{MM:02d}" #En caso afirmativo se devuelve en formato string HH:MM (agregando ceros a la izquierda)
    else:
        return False #Caso contrario se retorna falso

#Programa principal
#Inicialización de variables

dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo") #Tupla que almacena días de la semana para validación

agenda = {("lunes", "10:00") : "Reunión", ("lunes", "12:00") : "Almuerzo con cliente", ("lunes", "16:00") : "Gimnasio", ("martes", "10:00") : "Videoconferencia", 
          ("martes", "18:30") : "Terapia", ("miércoles", "14:40") : "Pediatra", ("jueves", "08:00") : "Taller", ("viernes", "20:00") : "Asado"} #Agenda con valores predeterminados
booleano = True #Variable que controla el bucle principal

print("\nBienvenido al servicio de agenda\n")

while booleano: #Se repite hasta que el usuario desee salir
    dia_consulta = input("Por favor, ingrese el día de la semana que desea consultar: ").strip().lower()
    if dia_consulta not in dias_semana: #Se compara el valor ingresado con la tupla de días de la semana para validar
        print("El valor ingresado no es un día de la semana.")
        booleano = validacion() #Verifica con el usuario si desea seguir
        continue #Se salta el resto del bucle
    horas = input(f"Ingrese la hora que desea consultar (HH): ").strip
    minutos = input(f"Ingrese los minutos que desea consultar (MM): ").strip

    hora_consulta = check_horario(horas, minutos) #Se llama a la función que verifica el formato de la hora
    if hora_consulta == False: #Si la función retornó falso se informa y verifica con si el usuario desea seguir
        print("La hora ingresada no es correcta.")
        booleano = validacion()
        continue #Se salta el resto del bucle
    if agenda.get((dia_consulta,hora_consulta)) is None: #Si la clave no está cargada en el diccionario se informa al usuario
        print(f"\nNo hay actividad agendada para el día {dia_consulta} a las {hora_consulta}.")
    else: #Si hay datos almacenados se le muestran al usuario
        print(f"\nLa actividad agendada para el día {dia_consulta} a las {hora_consulta} es: {agenda[(dia_consulta,hora_consulta)]}.")
    booleano = validacion() #Verifica con el usuario si desea seguir

print("\n¡Gracias por usar la agenda!")

print("\n\n-------------Fin del ejercicio N° 9---------------\n")


# Ejercicio Nº 10
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 10---------------------------\n")

#Declaración de funciones

def impresion_diccionario(diccionario): #Función de impresión del diccionario
    for key, value in diccionario.items():
        print(f"- {key} : {value}")    
    return None

def inversion_diccionario(diccionario): #Función de impresión del diccionario
    for key, value in diccionario.items():
        print(f"- {key} : {value}")    
    return None

#Programa principal
#Inicialización de variables

paises = {"Argentina" : "Buenos Aires",  "Brasil" : "Brasilia", "Uruguay" : "Montevideo", "Chile" : "Santiago de Chile", "Paraguay" : "Asunción",  
          "Perú" : "Lima", "Bolivia" : "Sucre", "Colombia" : "Bogota", "Venezuela" : "Caracas"} #Diccionario con países como clave, capitales como valores

capitales = {} #Diccionario con capitales como clave, países como valores *VACÍO*

#Salida de datos originales:

print("\n----- Base de datos de países y sus capitales -----\n ")

impresion_diccionario(paises) #Se llama a la función que imprime el diccionario

for clave, valor in paises.items(): #Se recorre el diccionario original y se carga el nuevo invirtiendo los valores
    capitales[valor] = clave

print("\n----- Base de datos de capitales y sus respectivos países -----\n")

impresion_diccionario(capitales) #Se llama a la función de impresión para imprimir el nuevo diccionario

print("\n\n-------------Fin del ejercicio N° 10---------------\n")


