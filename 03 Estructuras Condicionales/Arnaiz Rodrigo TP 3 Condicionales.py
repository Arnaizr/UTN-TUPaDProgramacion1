#--------------Práctica Nº 3--------------#
#--------Estructuras Condicionales--------#

#Ejercicio Nº 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Inicio de programa
print("Ejercicio 1:")
#Carga de datos
edad = int(input("Hola, por favor ingrese la edad del usuario: "))
#Inicio de estructura condicional para verificar si el usuario es mayor de edad
if edad >= 18:
    #Salida de información
    print("Es mayor de edad")
#Fin de estructura condicional
#Fin del programa

# Ejercicio Nº 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”
# Inicio de programa

print("Ejercicio 2:")
#Carga de datos
nota = float(input("Hola, por favor ingresar la nota del usuario: "))
#Inicio de estructura condicional para verificar la condición de aprobado
if nota >= 6:
    #Salida de información
    print("Aprobado.")
#else:
    print("Desaprobado.")
#Fin de estructura condicional
#Fin de programa

#Ejercicio Nº 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#Inicio de programa
print("Ejercicio 3:")
#Carga de datos
num = int(input("Hola, por favor ingresar un número par: "))
#Procesamiento de datos
resto = num % 2 #Se verifica que el resto de la división por dos sea cero
#Inicio de estructura condicional para verificar si el número es par
if resto == 0:
    #Salida de información
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")
#Fin de estructura condicional
#Fin del programa

#Ejercicio Nº 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

#Inicio de programa
print("Ejercicio 4:")
#Carga de datos
edad = int(input("Hola, por favor ingresar la edad del usuario: "))
#Inicio de la estructura condicional para determinar la franja etaria con devolución de información
if edad >= 0 and edad < 12:
    print("El usuario es un/a niño/a.")
elif edad >= 12 and edad < 18:
    print("El usuario es un/a adolescente.")
elif edad >= 18 and edad < 30:
    print("El usuario es un/a adulto/a joven.")
elif edad >= 30 and edad <= 120:
    print("El usuario es un/a adulto.") #Se determina un valor máximo de 120 años
else:
    print("La edad ingresada no es válida.") #Se muestra este mensaje si se ingresa un valor menor a cero o mayor a 120.
#Fin del condicional
#Fin del Programa

# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

#Inicio de programa
print("Ejercicio 5:")
#Carga de datos
contrasenia = str(input("Hola, por favor ingrese una contraseña entre 8 y 14 caracteres: "))
#Cálculo de longitud de la contraseña
longitud = len(contrasenia)
#Inicio de la estructura condicional para determinar si la contraseña es adecuada con devolución de información
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
#Fin del condicional
#Fin del programa

# Ejercicio 6
# El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

#Inicio del programa
print("Ejercicio 6:")
#Importación de funciones de estadística
from statistics import mode, median, mean
#Importación de función de números aleatorios
import random
#Creación de la lista de números aleatorios
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#Declaración de variables con el resultado de las funciones de estadística sobre la lista
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#Estructura condicional para determinar el tipo de sesgo de la lista con devolución de datos
if moda == mediana and moda == media:
    print("La lista generada no tiene sesgo.")
elif media > mediana and mediana > moda:
    print("La lista generada tiene sesgo positivo.")
elif media < mediana and mediana < moda:
    print("La lista generada tiene sesgo negativo.")
# Se deja como posible una salida más de la estructura condicional en el caso de querer devolver un mensaje al usuario
# si no se da ninguno de las combinaciones planteadas ya que son muchos los casos en que no se devuelve esa información
# else:
#     print("La lista generada tiene un sesgo no definido en la consigna.")
#Fin de estructura condicional
#Fin del programa

# Ejercicio 7:
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("Ejercicio 7:")
#Carga de datos
palabra = str(input("Hola, por favor ingresar una palabra: "))
#Procesamiento de datos
ultimo_caracter = palabra[-1] #Se extrae el último caracter del string por su índice
#Inicio de condicional para verificar si el último caracter es una vocal
if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
    palabra = palabra + "!" #Se agrega el signo de admiración en caso afirmativo
#Fin del condicional
#Salida de información
print(f"La palabra o frase ingresada fue {palabra}.")
#Fin del programa

# Ejercicio 8:
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("Ejercicio 8:")
#Carga de datos
nombre = str(input("Hola, por favor ingrese su nombre: "))
opcion = int(input("Por favor, ingrese (1) si quiere su nombre en mayúsculas, (2) si lo quiere en minúsculas o (3) si quiere la primer letra mayúscula: "))
#Inicio de condicional según la opción elegida
if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
#Fin del condicional
#Salida de información
print(f"Su nombre de acuerdo a la opción seleccionada es: {nombre}.")
#Fin del programa

#Ejercicio 9:
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ejercicio 9:")
#Carga de datos
magnitud = float(input("Hola, por favor ingrese la magnitud de un terremoto: "))
#Inicio de estructura condicional según la magnitud ingresada
if magnitud >= 0 and magnitud < 3:
    mensaje = "muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    mensaje = "leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    mensaje = "moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    mensaje = "fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    mensaje = "muy Fuerte (puede causar daños significativos)"
elif magnitud >= 7 and magnitud < 10:
    mensaje = "extremo (puede causar graves daños a gran escala)"
else:
    mensaje = "un valor no válido para la escala" #Se agrega esta opción en caso de números negativos o mayores a los jamás registrados
#Fin del condicional
#Salida de información
print (f"Un terremoto de magnitud {magnitud} en escala Ritcher es {mensaje}.")
#Fin del programa

# Ejercicio 10
# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

#     Periodo del año         Estación en el              Estación en el
#                            hemisferio norte             hemisferio sur

# Desde el 21 de diciembre 
# hasta el 20 de marzo           Invierno                     Verano
# (incluidos)

# Desde el 21 de marzo 
# hasta el 20 de junio          Primavera                     Otoño
# (incluidos)

# Desde el 21 de junio 
# hasta el 20 de                 Verano                      Invierno
# septiembre (incluidos)

# Desde el 21 de septiembre 
# hasta el 20 de                 Otoño                       Primavera
# diciembre (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("Ejercicio 10:")
#Carga de datos
hemisferio = str(input("Hola, por favor ingrese el hemisferio en el que se encuentra (N/S): "))
mes = str(input("Por favor, ingresar el mes actual: "))
dia = int(input("Por favor, ingresar el día actual: "))
#Procesasmiento de datos
mes = mes.lower() #se transforma la variable a minúscula para evitar discordancias en el ingreso de los meses
hemisferio = hemisferio.upper() #se transforma la variable a mayúscula en el caso que se haya ingresado minúscula
#Inicialización de una variable booleana en caso de ingresos erróneos de datos
bool = True
#Inicio de una estructura condicional que ejecuta el código en el caso que el valor del día esté en el rango correcto
if dia >= 1 and dia <= 31:
    #Inicio de estructura condicional para corroborar el hemisferio
    if hemisferio == "S":
        #Inicio de estructura condicional para verificar el mes y día para asignar la estación en hemisferio sur
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia < 21):
            estacion = "verano"
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia < 21):
            estacion = "otoño"
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia < 21):
            estacion = "invierno"
        elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia < 21):
            estacion = "primavera"
        else:
            bool = False #Se cambia el valor de la variable en el caso que el mes ingresado no sea válido
        #Fin de estructura condicional que verifica la estación en el hemisferio sur
        hemisferio = "sur" #se convierte la variable a una palabra para una visual más estética en el mensaje de salida
        #Fin de la primera condición de salida
    elif hemisferio == "N":
        #Inicio de la condición alternativa para verificar el mes y día para asignar la estación en hemisferio norte
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia < 21):
                estacion = "invierno"
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia < 21):
                estacion = "primavera"
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia < 21):
            estacion = "verano"
        elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia < 21):
            estacion = "otoño"
        else:
            bool = False #Se cambia el valor de la variable en el caso que el mes ingresado no sea válido
        #Fin de estructura condicional que verifica la estación en el hemisferio norte
        hemisferio = "norte" #se convierte la variable a una palabra para una visual más estética en el mensaje de salida
    else:
        bool = False #Se cambia el valor de la variable en el caso que el hemisferio ingresado no sea válido
    #Fin de la estructura condicional del hemisferio
else:
    bool = False #Se cambia el valor de la variable en el caso que el día ingresado no esté en el rango válido. Se aceptan
                 #valores que no corresponden al mes si están dentro del rango (Ejemplo: febrero de 30 días).
#Fin de la estructura condicional que verifica el valor de los días.
#Inicio de estructura condicional que controla el mensaje de salida
if bool: #Si la variable mantiene un valor "True" los datos fueron cargados con valores correctos.
    print(f"Te encuentras en el hemisferio {hemisferio}, hoy es {dia} de {mes}, y es un bello día de {estacion}!.")
else:
     print("Lamentablemente, uno de los valores ingresados fue incorrecto, por favor empezar nuevamente.")
#Fin de estructura condicional que entrega el mensaje de salida
#Fin del programa

#-------------------------- Fin del Trabajo Práctico Nº 3--------------------------#