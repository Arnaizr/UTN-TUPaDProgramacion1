#---------------------------------------------------PRÁCTICA Nº 5--------------------------------------------------#
#------------------------------------------------------LISTAS------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


#Ejercicio Nº 1
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 1---------------------------\n")
#Importación de función aleatoria
import random
#Inicialización de variables
notas = []
notamax = -1 #Se inicializa en -1 para asegurar que aunque sea un valor será mayor
notamin = 11 #Se inicializa en 11 para asegurar que aunque sea un valor será menor
sumatoria = 0 #Variable que acumula las notas
#Inicialización de bucle que carga notas aleatorias para los alumnos y calcula resultados
for i in range (10): 
    notas.append(random.randint(0,10))
    sumatoria += notas[i] #Se acumula el valor que se carga en el índice actual
    if (notamax < notas[i]): #Controla el valor máximo de notas con el indice actual
        notamax = notas[i] #Reemplaza el valor máximo de notas con el indice actual
    elif (notamin > notas[i]): #Controla el valor minimo de notas con el indice actual
        notamin = notas[i] #Reemplaza el valor minimo de notas con el indice actual
#Salida de datos
print(f"Las notas de los alumnos son:", end= " ") #Punto 1: Mostrar la lista completa 
for i in notas:
    print(i, end=" ")
print(f"\n\nEl promedio de notas de todos los alumnos es: {sumatoria/10}.") #Punto 2: Calcular y mostrar el promedio
print(f"\nLa nota más alta fue un {notamax} y la nota más baja fue un {notamin}.") #Punto 3: Indicar la nota más alta y la nota más baja
print("\n-----------------------Fin del Ejercicio Nº 1-----------------------\n")


#Ejercicio Nº 2
# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 2---------------------------\n")
#Inicialización de variables
productos = []
prod_a_eliminar = ""
#Inicio de bucle que carga la lista
for i in range (5):
    productos.append(input("Por favor, ingrese un producto a la lista: "))
productos = sorted(productos)
print("\nLos productos cargados en orden son:", end=" ") #Punto 1: Se muestra la lista ordenada
for i in productos:
     print(i, end=" ")
#Se solicita al usuario el producto que desea eliminar
prod_a_eliminar = input("\n\nPor favor, ingrese el producto que desea eliminar: ")
#Se verifica que el producto esté en la lista
if prod_a_eliminar in productos:
    productos.remove(prod_a_eliminar) #Se elimina el elemento de la lista
    print("\nLa lista actualizada es:", end=" ") #Punto 2: se muestra la lista sin el producto a eliminar
    for i in productos:
        print(i, end=" ")
else:
    print(f"\nEl producto {prod_a_eliminar} no está en la lista!", end=" ")
print("\n\n-----------------------Fin del Ejercicio Nº 2-----------------------\n\n")

#Ejercicio 3
# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 3---------------------------\n")
#Importación de función aleatoria
import random
#Inicialización de variables
lista_inicial = []
lista_par = []
lista_impar = []
#Bucle que carga la lista con valores aleatorios
for i in range (15): 
    lista_inicial.append(random.randint(1,100)) #Se crea una lista con los 15 números al azar
    if (lista_inicial[i] % 2) == 0:
        lista_par.append(lista_inicial[i]) #Si el valor es par se agrega a la lista de pares
    else:
        lista_impar.append(lista_inicial[i]) #Si el valor es impar se agrega a la lista de impares
#Fin del bucle
#Salida de datos
#Muestra la lista generada
print(f"La lista de números generada es:", end=" ")
for i in lista_inicial:
     print(i, end=" ")
#Muestra la lista de números pares y la cantidad de elementos
print(f"\n\nLa lista de números pares es:", end=" ")
for i in lista_par:
     print(i, end=" ")
print(f"y tiene {len(lista_par)} elementos.")
#Muestra la lista de númerso impares y la cantidad de elementos
print(f"\nLa lista de números impares es:", end=" ")
for i in lista_impar:
    print(i, end=" ")
print(f"y tiene {len(lista_impar)} elementos.")
print("\n-----------------------Fin del Ejercicio Nº 3-----------------------\n\n")

#Ejercicio Nº 4
# 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 4---------------------------\n")
#Creación de lista de la consigna
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#Inicialización de lista sin repetidos
sin_repetidos = []
#Inicio de bucle que recorre la lista
for i in datos:
    if i not in sin_repetidos: #Condicional que va incorporando los elementos de la lista sin repetirlos
        sin_repetidos.append(i)
#Fin del bucle
#Salida de datos
print("La lista original es:", end=" ")
for i in datos:
    print(i, end=" ")
print("\n\nLa lista sin valores repetidos es:", end=" ")
for i in sin_repetidos:
    print(i, end=" ")
# Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 4-----------------------\n\n")


# Ejercicio Nº 5
# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.


#Inicio del programa
print("\n---------------------------Ejercicio Nº 5---------------------------\n")
#Inicialización de variables
alumnos = []
#Creación de una lista con nombres de estudiantes
while len(alumnos) < 8:
    alu_actual = input("\nPor favor, ingrese el nombre de un alumno de la clase: ")
    presente = input(f"¿El/la alumno/a {alu_actual} está presente? (Si/No) ")
    presente.lower #Se minimiza la respuesta para el condicional
    if presente == "si" or presente == "s":
        alumnos.append(alu_actual) #Si el alumno está presente se agrega a la lista
#Fin de incorporación de alumnos
#Muestreo de la lista terminada
print("\nLa lista de 8 alumnos presentes es:", end=" ")
for i in alumnos:
    print(i, end=" ")
#Se consulta si se desea agregar o sacar un alumno
cambiar_lista = input("\n¿Desea incorporar un nuevo estudiante a la lista? (Si/No) ")
cambiar_lista.lower
if cambiar_lista == "si" or cambiar_lista == "s":
    alumnos.append(input("\nIngrese el nombre del alumno a ingresar: "))
    cambiar_lista = input("\n¿Desea eliminar un estudiante de la lista? (Si/No) ")
    cambiar_lista.lower
    if cambiar_lista == "si" or cambiar_lista == "s":
        alu_actual = input("\nPor favor, ingrese el nombre del alumno que desea eliminar: ")
        if alu_actual in alumnos:
            alumnos.remove(alu_actual)
        else:
            print(f"\nEl/la alumno/a {alu_actual} no está en la lista!")
elif cambiar_lista == "no" or cambiar_lista == "n":
    cambiar_lista = input("\n¿Desea eliminar un estudiante de la lista? (Si/No) ")
    cambiar_lista.lower
    if cambiar_lista == "si" or cambiar_lista == "s":
        alu_actual = input("\nPor favor, ingrese el nombre del alumno que desea eliminar: ")
        if alu_actual in alumnos:
            alumnos.remove(alu_actual)
        else:
            print(f"\nEl/la alumno/a {alu_actual} no está en la lista!")
#Salida de datos
print("\nLa lista final de alumnos presentes es:", end=" ")
for i in alumnos:
    print(i, end=" ")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 5-----------------------\n\n")



# Ejercicio Nº 6
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

#Inicio del programa
print("\n---------------------------Ejercicio Nº 6---------------------------\n")
#Se importa la función random
import random
#Inicialización de variables
lista = []
#Creación de la lista con 7 números
for i in range (7): 
    lista.append(random.randint(0,99)) #Se crea una lista con 7 números al azar
#Fin del bucle
#Se muestra la lista generada
print("\nLa lista de 7 números generada es:", end=" ")
for i in lista:
    print(i, end=" ")
aux = lista[6] #Se almacena el valor del último índice de la lista
for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i-1] #Desplazandose de derecha a izquierda, se van almacenando los valores del próximo indice en el actual                                                            
lista[0] = aux #Se guarda en el primer lugar el último valor de la lista
print("\n\nLa lista de 7 números desplazada es:", end=" ")
for i in lista:
    print(i, end=" ")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 6-----------------------\n\n")

# Ejercicio Nº 7
# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica

#Inicio del programa
print("\n---------------------------Ejercicio Nº 7---------------------------\n")
#Inicialización de variables
matriz = []
temp_nombre = "" #Se declara una variable para asignar nombre a la temperatura máxima o mínima
amplitud_max = -1.0 #Para almacenar la mayor amplitud térmica
dia_mayor_amp = -1.0 #Para almacenar el día con la mayor amplitud térmica
minimas = 0 #Para acumular las temperaturas mínimas
maximas = 0 #Para acumular las temperaturas máximas
for fila in range(7):
    fila_dia = [] #Se crea la nueva lista para almacenar las temperaturas del día
    for columna in range(2):
        if columna == 0:
            temp_nombre = "mínima"
        else:
            temp_nombre = "máxima"
        match fila:
            case 0:
                dia = "lunes"
            case 1:
                dia = "martes"
            case 2:
                dia = "miércoles"
            case 3:
                dia = "jueves"
            case 4:
                dia = "viernes"
            case 5:
                dia = "sábado"
            case 6:
                dia = "domingo"
        temp_actual = float(input(f"\nPor favor, ingrese la temperatura {temp_nombre} del {dia}: ")) #Se ingresa la temperatura mínima y máxima del día correspondiente
        fila_dia.append(temp_actual) #Se agrega la temperatura cargada a las correspondientes al día
        if  columna == 0:
            minimas += temp_actual #Acumula todas las temperaturas mínimas ingresadas
        else:
            maximas += temp_actual #Acumula todas las temperaturas máximas ingresadas
    matriz.append(fila_dia) #Se agregan las temperaturas de ese día en la matriz
#Fin de la carga de las temperaturas de la semana
#Se recorren todos los días para calcular la amplitud de cada día
for i in range(len(matriz)):
    min_dia = matriz[i][0] #Se almacena la temperatura mínima del día "i"
    max_dia = matriz[i][1] #Se almacena la temperatura máxima del día "i"

    amplitud_dia = max_dia - min_dia #Se calcula la amplitud térmica del día "i"

    if amplitud_dia > amplitud_max: 
        amplitud_max = amplitud_dia #Se almacena la mayor amplitud térmica
        dia_mayor_amp = i #Se almacena el día la mayor amplitud térmica
#Creacion de una lista con los días de la semana para mostrar la matriz
dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
#Salida de información
print("\nLas temperaturas de la semana fueron: ")
for i in range(len(matriz)):
    print(f"{dias_semana[i]}    Min: {matriz[i][0]}     Max:  {matriz[i][1]}")
print(f"\nEl promedio de las temperaturas mínimas fue: {minimas/7}.")
print(f"\nEl promedio de las temperaturas máximas fue: {maximas/7}.")
match dia_mayor_amp: #Se asigna a la variable día el dia con mayor amplitud para mejor estética visual
    case 0:
        dia = "lunes"
    case 1:
        dia = "martes"
    case 2:
        dia = "miércoles"
    case 3:
        dia = "jueves"
    case 4:
        dia = "viernes"
    case 5:
        dia = "sábado"
    case 6:
        dia = "domingo"
print(f"\nEl día con mayor amplitud térmica fue el {dia} con una amplitud de {amplitud_max}ºC.")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 7-----------------------\n\n")


# Ejercicio Nº 8
# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 8---------------------------\n")
#Inicialización de variables
materias = [] #Lista que almacena las materias de las que se solicitarán las notas
matriz_notas = [] #Matriz que almacenará todas las notas de los alumnos
#Ingreso de datos
for i in range(3): #Se crea un bucle para elegir las materias de las que se solicitarán las notas
    materias.append(input(f"Por favor, ingrese la {i+1}º materia de las que desea ingresar las notas: "))
#Se crea un nuevo bucle para cargar la matriz
for fila in range(5): #El primer bucle carga la fila de cada alumno:
    alumno = [] #Se crea la nueva lista para almacenar los datos del cada alumno 
    for j in range(4): #Se crea una la nueva lista con nombre de cada alumno y sus notas
        if j == 0: #Condicional para asegurar que el primer valor de cada fila sea el nombre del alumno
            alumno.append(input(f"\nPor favor, ingrese apellido y nombre del {fila+1}º alumno: "))
        else:
            match j: #Condicional para una mejor visualización al solicitar la nota de cada materia
                case 1:
                    materia = materias[j-1] #Se deja con el valor "j-1" en caso de querer agregar más materias
                case 2:
                    materia = materias[j-1] #Se deja con el valor "j-1" en caso de querer agregar más materias
                case 3:
                    materia = materias[j-1] #Se deja con el valor "j-1" en caso de querer agregar más materias
            #Solicitud de carga de notas del alumno por materia
            alumno.append(float(input(f"Por favor, ingrese la nota de {alumno[0]} en {materia}: ")))
        #Fin del condicional para cargar los datos del alumno
    #Fin del bucle para cargar los datos del alumno
    matriz_notas.append(alumno) #Se agrega la fila de cada alumno a la matriz
promedios_alumnos = [] #Lista para almacenar los promedios de los alumnos
promedios_materias = [] #Lista para almacenar los promedios por materia
# Inicio de bucle para almacenar los promedios de los alumnos
for i in range(len(matriz_notas)):
    suma_notas = 0
    for j in range(len(matriz_notas[0])-1): #Se toma el rango menos uno para no usar el valor del nombre
        suma_notas += matriz_notas[i][j+1] #Se toma el valor i+1 para no tomar los valores del nombre
    suma_notas = round((suma_notas/(len(matriz_notas[0])-1)), 2) #Se calcula el promedio de notas del alumno "i"
    promedios_alumnos.append(suma_notas) #Se almacena la lista el promedio de cada alumno
#Fin del bucle para almacenar los promedios de los alumnos
# Inicio de bucle para almacenar los promedios de las materias
for i in range(len(matriz_notas[0])-1): #Se toma el rango menos uno para no usar el valor del nombre
    suma_materia = 0
    for j in range(len(matriz_notas)):
        suma_materia += matriz_notas[j][i+1] #Se toma el valor i+1 para no tomar los valores del nombre
    suma_materia = round((suma_materia/(len(matriz_notas))), 2) #Se calcula el promedio de notas de la materia "j+1"
    promedios_materias.append(suma_materia) #Se almacena en la lista el promedio de cada materia
#Fin del bucle para almacenar los promedios de las materias
#Salida de información
#Impresión de la matriz con las notas
print("\nAlumno |", end=" ")
for i in range(len(materias)):
    print(materias[i], end=" | ")
print("")
for i in range(len(matriz_notas)):
    for j in range(len(matriz_notas[0])):
        print(f"{matriz_notas[i][j]}", end="   |   ")
    print("\n")
#Impresión de los promedios de los alumnos
for i in range(len(promedios_alumnos)):
    print(f"El promedio del alumno {matriz_notas[i][0]} es: {promedios_alumnos[i]}.")
#Impresión de los promedios de las materias
print("")
for i in range(len(promedios_materias)):
    print(f"El promedio de los alumnos en {materias[i]} es: {promedios_materias[i]}.")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 8-----------------------\n\n")


# Ejercicio Nº 9
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

#Inicio del programa
print("\n---------------------------Ejercicio Nº 9---------------------------\n")
#Inicialización de variables
matriz_tateti = []
#Carga de la matriz
for i in range(3):
    fila_tateti = []
    for j in range(3):
        fila_tateti.append(" - ")
    matriz_tateti.append(fila_tateti)
print("Juguemos al Ta-Te-Tí!\n")
for i in range(3):
            for j in range(3):
                print(matriz_tateti[i][j], end="")
            print("\n")
turno = 0 #Variable para controlar el turno de cada jugador
jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")
#Inicio del bucle para llenar el tablero
while " - " in matriz_tateti[0] or " - " in matriz_tateti[1] or " - " in matriz_tateti[2]: #Se verifica que queden casilleros sin completar
    fila = 0 #Se inicializa la variable fila para cada turno
    columna = 0 #Se inicializa la variable columna para cada turno
    if (turno % 2) == 0: #Se verifica si el turno es par o impar para asignarlo a cada jugador (comenzando en cero)
        print(f"\nEs el turno de {jugador1}.")
        while fila == 0: #Se repite el bucle hasta que se ingrese una casilla válida 
            fila = int(input("Por favor, indicá el número de fila (1 o 2 o 3): ")) #Se solicita el ingreso de la fila
            if fila > 0 and fila <= 3: #Se verifica que la fila esté en un rango válido
                columna = int(input("Por favor, indicá el número de columna (1 o 2 o 3): ")) #Se solicita el ingreso de la columna
                if columna > 0 and columna <= 3: #Se verifica que la columna esté en un rango válido
                    if matriz_tateti[fila-1][columna-1] == " - ": #Se verifica que la celda no haya sido ocupada
                        matriz_tateti[fila-1][columna-1] = " X " #Se reemplaza el valor por el símbolo del jugador 1
                    else:
                        print(f"\n¡La casilla {fila} x {columna} ya fue ocupada! Intentá otra.\n")
                        fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
                else:
                    print(f"\n¡La columna {columna} no está en el tablero! Intentá otra.\n")
                    fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
            else:
                print(f"\n¡La fila {fila} no está en el tablero! Intentá otra.\n")
                fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
        turno += 1 #Se incrementa el contador del turno
        #Muestreo del tablero al finalizar el turno
        print(f"\nFin del {turno}º turno:\n")
        for i in range(3):
            for j in range(3):
                print(matriz_tateti[i][j], end="")
            print("\n")
    else:
        print(f"\nEs el turno de {jugador2}.") #Si el turno es impar le corresponde al jugador 2
        while fila == 0: #Se repite el bucle hasta que se ingrese una casilla válida
            fila = int(input("Por favor, indicá el número de fila (1 o 2 o 3): ")) #Se solicita el ingreso de la fila
            if fila > 0 and fila <= 3: #Se verifica que la fila esté en un rango válido
                columna = int(input("Por favor, indicá el número de columna (1 o 2 o 3): ")) #Se solicita el ingreso de la columna
                if columna > 0 and columna <= 3:  #Se verifica que la columna esté en un rango válido
                    if matriz_tateti[fila-1][columna-1] == " - ": #Se verifica que la celda no haya sido ocupada
                        matriz_tateti[fila-1][columna-1] = " O "  #Se reemplaza el valor por el símbolo del jugador 2
                    else:
                        print(f"\n¡La casilla {fila} x {columna} ya fue ocupada! Intentá otra.\n")
                        fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
                else:
                    print(f"\n¡La columna {columna} no está en el tablero! Intentá otra.\n")
                    fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
            else:
                print(f"\n¡La fila {fila} no está en el tablero! Intentá otra.\n")
                fila = 0 #Se reinicia el valor de la fila para mantenerse en el bucle
        turno += 1 #Se incrementa el contador del turno
        #Muestreo del tablero al finalizar el turno
        print(f"\nFin del {turno}º turno:\n")
        for i in range(3):
            for j in range(3):
                print(matriz_tateti[i][j], end="")
            print("\n")
#Se sale del bucle una vez que todas las casillas están ocupadas (sin el campo ' - ')
print("¡Se terminó! ¡Gracias por jugar!")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 9-----------------------\n\n")


#Ejercicio Nº 10
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

# Inicio del programa
print("\n---------------------------Ejercicio Nº 10---------------------------\n")

#Inicialización de variables
matriz_productos = [] #Matriz que almacenará los productos y las cantidades de ventas
ventas_prod = [] #Lista que almacena las ventas de cada producto
dia_maximo = 0 #Almacena la máxima cantidad de ventas por día
indice_dia = 0 #Almacena el índice del día con más ventas
producto_max = 0 #Almacena el producto con más ventas en la semana
indice_prod = 0 #Almacena el índice del producto con más ventas
#Ingreso de datos
#Se crea un bucle para cargar la matriz
for i in range(4): #El primer bucle carga la fila de cada cada producto:
    ventas_semanal = 0 #Se inicializa el acumulador de ventas para el producto "i"
    producto = [] #Se crea la nueva lista para almacenar los datos de cada producto 
    for j in range(8): #Se crea una la nueva lista con el nombre de cada producto y sus ventas semanales
        if j == 0: #Condicional para asegurar que el primer valor de cada fila sea el nombre del producto
            producto.append(input(f"\nPor favor, ingrese el nombre del {i+1}º producto a analizar: "))
            producto[j] = producto[j].upper() #Se convierte a mayúsculas para mejor visualización
        else:
            match j: #Condicional para una mejor visualización al solicitar las ventas de cada producto
                case 1:
                    dia = "lunes"
                case 2:
                    dia = "martes"
                case 3:
                    dia = "miércoles"
                case 4:
                    dia = "jueves"
                case 5:
                    dia = "viernes"
                case 6:
                    dia = "sábado"
                case 7:
                    dia = "domingo"                
            #Solicitud de carga de ventas del producto cada día
            producto.append(int(input(f"Por favor, ingrese la cantidad de ventas del producto *{producto[0]}* el día {dia}: ")))
            ventas_semanal += producto[j] #Se acumula el total de ventas del producto "i"
        #Fin del condicional para cargar los datos del producto
    #Fin del bucle para cargar los datos del producto "i"
    ventas_prod.append(ventas_semanal) #Se almacena en la lista el total de ventas del producto "i"
    matriz_productos.append(producto) #Se agrega la fila de cada producto a la matriz
#Fin del bucle para cargar la matriz
# Inicio de bucle para calcular el día de mayor cantidad de ventas
for i in range(len(matriz_productos[0])-1): #Se toma el rango menos uno para no usar el valor del nombre
    suma_dia = 0
    #Inicio del bucle que acumula el total de ventas por cada día
    for j in range(len(matriz_productos)):
        suma_dia += matriz_productos[j][i+1] #Se toma el valor i+1 para no tomar los valores del nombre
    #Fin del bucle que acumula el total de ventas por cada día
    #Condicional que verifica si las ventas del día "i+1" son mayores al máximo de ventas por día
    if suma_dia > dia_maximo:
        dia_maximo = suma_dia
        indice_dia = i+1
#Fin del bucle para calcular el día con más ventas
#Inicio de bucle para calcular el producto con más ventas
for i in range(len(ventas_prod)):
    if ventas_prod[i] > producto_max: #Se verifica la cantidad de ventas de cada producto con el máximo (inicializado en 0)
        producto_max = ventas_prod[i] #Se actualiza el producto con más ventas
        indice_prod = i #Se almacena el índice del producto con más ventas
#Fin del bucle para calcular el producto con más ventas
match indice_dia: #Condicional para una mejor visualización al mostrar el día con mas ventas
                case 1:
                    dia = "lunes"
                case 2:
                    dia = "martes"
                case 3:
                    dia = "miércoles"
                case 4:
                    dia = "jueves"
                case 5:
                    dia = "viernes"
                case 6:
                    dia = "sábado"
                case 7:
                    dia = "domingo"
#Salida de información
print("\nProducto | Lun | Mar | Mie | Jue | Vie | Sab | Dom |") #Lista para mejor visualización de la matriz
#Impresión de la matriz con las ventas de cada producto por día
for i in range(len(matriz_productos)):
    for j in range(len(matriz_productos[0])):
        print(f"{matriz_productos[i][j]}", end="  |  ")
    print("\n")
#Impresión del total de ventas de cada producto
for i in range(len(ventas_prod)):           
    print(f"El total de ventas del producto *{matriz_productos[i][0]}* en la semana fueron {ventas_prod[i]} ventas.")
#Impresión del día con mayor cantidad de ventas
print(f"\nEl día con mayor cantidad de ventas fue el {dia} con un total de {dia_maximo} ventas.")
#Impresión del producto con más cantidad de ventas
print(f"\nLo más vendido en la semana fue el producto *{matriz_productos[indice_prod][0]}* con un total de {producto_max} ventas.")
#Fin del programa
print("\n\n-----------------------Fin del Ejercicio Nº 10-----------------------\n\n")

#----------------------------------------------FIN DE LA PRÁCTICA Nº 5---------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#