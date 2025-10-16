#---------------------------------------------------PRÁCTICA Nº 6--------------------------------------------------#
#-----------------------------------------------------FUNCIONES----------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


#Ejercicio N° 1
#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 1---------------------------\n")

#--------Definición de funciones--------

def imprimir_hola_mundo():
    print("Hola Mundo!") #Se llama a la función print para imprimir el mensaje por pantalla

#--------Programa principal--------

imprimir_hola_mundo() #Llamada a la función

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 1-----------------------\n")




#Ejercicio N° 2
#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: 
#“Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.


#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 2---------------------------\n")

#--------Definición de funciones--------

def saludar_usuario(nombre):
    print(f"\nHola {nombre}!") #Se llama a la función print para imprimir el mensaje por pantalla con el parámetro recibido

#--------Programa principal--------

#Solicitud de ingreso de datos
nombre = input("Por favor, ingrese el nombre del usuario: ")
saludar_usuario(nombre)

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 2-----------------------\n")




#Ejercicio N° 3
#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.



#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 3---------------------------\n")

#--------Definición de funciones--------

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") #Se llama a la función print para imprimir el mensaje por pantalla con los parámetros recibidos

#--------Programa principal--------

#Inicialización de variables
datos = ["nombre", "apellido", "edad", "residencia"] #Se carga una lista con los datos a solicitar
#Solicitud de ingreso de datos
for i in range(len(datos)):
    datos[i] = input(f"Por favor, ingresar {datos[i]} del usuario: ") #Se reemplaza cada elemento de la lista por el dato ingresado por el usuario
    datos[i] = datos[i].title() #Se capitaliza la primera letra del nombre
informacion_personal(datos[0], datos[1], datos[2], datos[3]) #Llamada a la función con los parámetros ingresados

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 3-----------------------\n")




# Ejercicio N° 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# Calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 4---------------------------\n")

#--------Definición de funciones--------

def calcular_area_circulo(radio):
    area = round((3.1415926 * radio ** 2), 2) #Se calcula el área y se redondea a 2 decimales
    return area

def calcular_perimetro_circulo(radio):
    perimetro = round((3.1415926 * 2 * radio), 2) #Se calcula el perímetro y se redondea a 2 decimales
    return perimetro

#--------Programa principal--------

#Solicitud de ingreso de datos
radio = float(input("Por favor, ingrese el radio de un círculo: "))
#Salida de datos llamando a las 2 funciones
print(f"\nEl perímetro del círculo con un radio de {radio} unidades es de {calcular_perimetro_circulo(radio)} u.")
print(f"El área del círculo con un radio de {radio} unidades es de {calcular_area_circulo(radio)} u².")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 4-----------------------\n")





#Ejercicio N° 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 5---------------------------\n")

#--------Definición de funciones--------

def segundos_a_horas(segundos):
    resultado = []
    resultado.append(segundos // 3600) 
    segundos = segundos % 3600
    resultado.append(segundos // 60)
    resultado.append(segundos % 60)
    return resultado

#--------Programa principal--------

#Solicitud de ingreso de datos
segundos = int(input("Por favor, ingrese una cantidad de segundos para convertir a horas: "))
horas_minutos_segundos = segundos_a_horas(segundos)
print(f"\n{segundos} segundo/s corresponden a {horas_minutos_segundos[0]} hora/s, {horas_minutos_segundos[1]} minuto/s y {horas_minutos_segundos[2]} segundo/s.")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 5-----------------------\n")





#Ejercicio Nº 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 6---------------------------\n")

#--------Definición de funciones--------

def tabla_multiplicar(numero):
    tabla = []
    for i in range (1,11):
        tabla.append(numero*i)
    return tabla

#--------Programa principal--------

#Solicitud de ingreso de datos
numero = int(input("Por favor ingrese un número entero para conocer su tabla de multiplicar: "))
tabla = tabla_multiplicar(numero)
#Salida de información
print(f"La tabla de multiplicar del número {numero} es:\n")
for i in range (10):
    print(f"{numero} x {i+1} = {tabla[i]}")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 6-----------------------\n")






#Ejercicio Nº 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 7---------------------------\n")

#--------Definición de funciones--------

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    division = round(num1 / num2, 2)
    producto = num1 * num2
    return suma, resta, division, producto

#--------Programa principal--------

#Solicitud de ingreso de datos
numero1 = int(input("Por favor ingrese el primer número para operar: "))
numero2 = int(input("Por favor ingrese el segundo número para operar: "))

if numero2 == 0:
    print("¡El segundo número debe ser distinto de cero!")
else:
    resultado = operaciones_basicas(numero1, numero2)
    for i in range (len(resultado)):
        match i:
            case 0:
                operacion = "suma"
            case 1:
                operacion = "resta"
            case 2:
                operacion = "division"
            case 3:
                operacion = "multiplicación"
        print(f"El resultado de la {operacion} entre {numero1} y {numero2} es: {resultado[i]}")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 7-----------------------\n")






#Ejercicio Nº 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
# para mostrar el resultado con dos decimales.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 8---------------------------\n")

#--------Definición de funciones--------

def calcular_imc(peso, altura):
    return round(peso/(altura**2), 2)

def convertir_a_decimal(numero):
    numero = numero.replace("," , ".")
    numero = float(numero)
    return numero

#--------Programa principal--------

#Solicitud de ingreso de datos
peso = input("Por favor ingrese el su peso actual (en kilogramos): ")
altura = input("Por favor ingrese su altura (en metros): ")
#Invocación a función que convierte strings a flotantes (por si se ingresaron comas en vez de puntos)
peso = convertir_a_decimal(peso)
altura = convertir_a_decimal(altura)
#Invocación a la función y salida de información
print(f"\nSu Índice de Masa Corporal (IMC) es: {calcular_imc(peso, altura)}.")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 8-----------------------\n")







#Ejercicio Nº 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 9---------------------------\n")

#--------Definición de funciones--------

def celsius_a_farenheit(celsius):
    return round((celsius*9/5)+32, 2)

def convertir_a_decimal(numero):
    numero = numero.replace("," , ".")
    numero = float(numero)
    return numero

#--------Programa principal--------

#Solicitud de ingreso de datos
celsius = input("Por favor ingrese una temperatura en grados Celsius (°C): ")
#Invocación a función que convierte strings a flotantes (por si se ingresaron comas en vez de puntos)
celsius = convertir_a_decimal(celsius)
#Invocación a la función y salida de información
print(f"\n{celsius}°C equivalen a {celsius_a_farenheit(celsius)} grados Farenheit (°F).")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 9-----------------------\n")






# Ejercicio Nº 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 10---------------------------\n")

#--------Definición de funciones--------

def calcular_promedio(a, b, c):
    return round((a+b+c)/3, 2)

def convertir_a_decimal(numero):
    numero = numero.replace("," , ".")
    numero = float(numero)
    return numero

#--------Programa principal--------

#Inicialización de variables
numeros = [] #Lista que almacena los números del usuario
#Solicitud de ingreso de datos
for i in range(3):
    numeros.append(input(f"Por favor, ingrese el {i+1}º número: "))
    #Invocación a función que convierte strings a flotantes (por si se ingresaron comas en vez de puntos)
    numeros[i] = convertir_a_decimal(numeros[i])

#Invocación a la función y salida de información
print(f"\nEl promedio entre {numeros[0]}, {numeros[1]} y {numeros[2]} es: {calcular_promedio(numeros[0], numeros[1], numeros[2])}.")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 10-----------------------\n")







#----------------------------------------------FIN DE LA PRÁCTICA Nº 6---------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#