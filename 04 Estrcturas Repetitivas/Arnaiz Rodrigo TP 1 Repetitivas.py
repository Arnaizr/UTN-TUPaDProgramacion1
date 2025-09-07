#--------------Práctica Nº 4--------------#
#---------Estructuras Repetitivas---------#

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 1
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#Inicio de programa
print ("Ejercicio Nº 1")
#Inicio de bucle de repetición incondicional
for i in range (101): #Se establece el rango hasta 101 dado que es excluyente
    print (i)
#Fin del bucle
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 2
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

#Inicio de programa
print ("Ejercicio Nº 2")
# Solicitud de ingreso de datos
numero = int(input("Hola, por favor ingrese un número entero: "))
#Inicialización de variable contador
if numero == 0:
    cont = 1 #Se inicializa como 1 ya que nunca entrará al bucle
else:
    cont = 0 #En el caso contrario se inicializa como 0 para contar dígitos en el bucle
#Inicialización del bucle que cuenta la cantidad de dígitos del número ingresado
while numero != 0: #Sale del bucle si no quedan más dígitos que extraer
    numero = int(numero/10) #Va extrayendo los dígitos del número ingresado de uno en uno
    cont += 1 #incrementa el contador por cada bucle (y por cada dígito extraído)
#Fin del bucle
#Salida de datos
print (f"La cantidad de dígitos del número ingresado es: {cont}.")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 3
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Inicio del programa
print ("Ejercicio Nº 3")
#Solicitud de ingreso de datos
num1 = int(input("Hola, por favor ingrese un número entero: "))
num2 = int(input("Hola, por favor ingrese otro número entero: "))
#Inicio de estructura condicional para verificar qué numero es el mayor
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1
#Fin de estrucura condicional
#Inicio de estructura condicional para verificar si los números son consecutivos o iguales (bucle infinito)
if (mayor-menor) <= 1:
    print(f"Los números {num1} y {num2} son consecutivos o iguales, no hay números comprendidos entre ellos.")
else:
    suma = 0 #Inicialización de la variable que acumula la sumatoria de los números intermedios.
    #Inicialización del bucle que va de los números comprendidos entre los números ingresados
    for i in range (menor+1, mayor):
        suma += i #acumula todos los valores que toma i
    #Fin del bucle
    #Salida de datos
    print(f"La sumatoria de los números comprendidos entre {num1} y {num2} es: {suma}.")
#Fin del condicional
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejecricio Nº 4
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

#Inicio del programa
print("Ejercicio Nº 4:")
#Inicialización de variable acumuladora
suma = 0
#Ingreso de datos
num = int(input("Hola, por favor ingrese un número para empezar a contar: "))
#Inicio del bucle acumulador de numeros ingresados
while num != 0:
    suma += num #Incrementa el acumulador con los números ingresados
    #Solicitud de un nuevo número
    num = int(input("Por favor ingresar un nuevo número para contar o salir con cero: "))
#Fin del bucle
#Salida de datos
print(f"La sumatoria de los números ingresados es: {suma}.")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 5
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Inicio del programa
print("Ejercicio Nº 5:")
#Importación de función aleatoria
import random
#Inicialización de variables
cont = 0
num = -1 #Se inicializa en menos uno para garantizar el ingreso al bucle
x = random.randint(0 , 9) #Genera el número aleatorio del 0 al 9
#Inicio del bucle que se repite si no se adivina el número
while num != x:
    cont += 1 #incrementa el contador por cada intento
    num = int(input("Adivina adivinador, ¿qué número pensé hoy?: ")) 
    #Inicio de estrucutra condicional que informa si se acertó
    if num != x:
        print("¡Fallaste! Intentalo otra vez!")
#Fin de estructura de repetición
#Salida de datos
if cont == 1:
    print("¡Increíble! ¡Adivinaste al primer intento!")
else:
    print(f"¡Correcto! Necesitaste {cont} intentos para ganarme, ¿podrás superarte la próxima vez?")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 6
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

#Inicio del programa
print("Ejercicio Nº 6")
#Inicio del bucle en orden decreciente
for i in range (100, -1, -2): #Se da inicio en 100 (inclusive), hasta -1 (exclusivo), decreciendo de 2 en 2
    print(i) #Imprime todos los valores que toma i, de 100 a 0
#Fin del bucle
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 7
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

#Inicio del programa
print("Ejercicio Nº 7")
#Ingreso de datos
num = int(input("Hola, por favor ingrese un número entero positivo: "))
#Bucle para forzar el ingreso de un entero positivo
while num <= 0:
    num = int(input("El número ingresado no es un entero positivo, por favor intente nuevamente: "))
#Inicializacion de una variable para la sumatoria
sumatoria = 0
#Inicio de un bucle que va desde cero hasta el número ingresado sin contarlo
for i in range (num):
    sumatoria += i #acumula los valores que toma i de cero hasta num-1
#Fin del bucle
print(f"La sumatoria de los números comprendidos entre 0 y {num} es: {sumatoria}.")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 8
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Inicio del programa
print("Ejercicio Nº 8: ")
#Inicialización de variables
contpar = 0 #Variable para contar enteros pares
contimp = 0 #Variable para contar enteros impares
contpos = 0 #Variable para contar enteros positivos
contneg = 0 #Variable para contar enteros negativos
#Solicitud de ingreso de datos
cantmax = int(input("Por favor, ingrese cuántos números desea ingresar: ")) #Se solicita al usuario la cantidad de enteros
#o puede cargarse el valor de enteros a ingresar
#Inicio del bucle de carga de números
for i in range (cantmax):
    #Se informa la cantidad de números restantes
    print(f"Falta/n ingresar {cantmax-i} número/s.")
    #Solicitud de ingreso de números
    num = int(input("Por favor ingresar un número: "))
    if num > 0: #Condición para verificar que el número sea positivo
        contpos += 1 #Contador de positivos
    elif num < 0: #Condición para verificar que el número sea negativo
        contneg += 1 #Contador de negativos
    if (num % 2) == 0: #Condición para verificar que el número sea par
        contpar += 1 #Contador de pares
    else:
        contimp += 1 #Contador de impares
#Fin del bucle
#Salida de datos
print(f"Se ingresaron en total {contpos} números positivos.")
print(f"Se ingresaron en total {contneg} números negativos.")
print(f"Se ingresaron en total {contpar} números pares.")
print(f"Se ingresaron en total {contimp} números impares.")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#

#Ejercicio Nº 10
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Inicio del programa
print("Ejercicio Nº 10:")
#Solicitud de ingreso de datos
numero = int(input("Por favor, ingrese el número que desea invertir: "))
#Almacenamiento del número en una variable auxiliar
aux = numero
#Inicialización de variables
numinv = 0 #Almacena el nuevo número invertido
#Función de valor absoluto para calcular el nuevo número
aux = abs(aux)
#inicio del bucle que extrae los dígitos menos significativos de número
while aux != 0:
    resto = aux % 10 #Se extrae el dígito menos significativo de la variable auxiliar
    numinv = (numinv * 10) + resto #Se va incorporando el dígito menos significativo extraído y desplazando
    #como más significativos los existentes
    aux = int(aux / 10) #Se elimina el dígito menos significativo
#Fin del bucle corta cuando ya se extrayeron todos los dígitos
#Estructura de control para verificar el signo del número original
if numero < 0:
    numinv = -numinv #Se cambia el signo si el número era negativo
#Salida de datos
print(f"El número ingresado ({numero}) invertido es: {numinv}.")
#Fin del programa

#-------------------------------------------------------------------------------------------------------------------#
#------------------------------------------FIN DEL TRABAJO PRÁCTICO Nº 4--------------------------------------------#
