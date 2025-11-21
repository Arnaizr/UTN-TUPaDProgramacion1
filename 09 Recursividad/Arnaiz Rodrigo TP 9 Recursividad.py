#---------------------------------------------------PRÁCTICA Nº 9--------------------------------------------------#
#---------------------------------------------------RECURSIVIDAD---------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


# #Ejercicio N° 1
# # Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# # función para calcular y mostrar en pantalla el factorial de todos los números enteros
# # entre 1 y el número que indique el usuario


# #--------Inicio del programa--------
# print("\n---------------------------Ejercicio Nº 1---------------------------\n")

# #--------Definición de funciones--------

# def factorial_recursiva(num): #Llamada a la función de factorial
#     return 1 if num == 0 else num*factorial_recursiva(num-1) #Vuelve a llamar a la función restando de a uno hasta que llega a cero

# def ingreso_nat_ok(num):
#     if not num.isdigit(): #Si no es un numero natural retorna None
#         return None
#     else:
#         return int(num) #Si es válido retorna el valor convertido de formato    


# #--------Programa principal--------

# #Solicitud de ingreso de datos

# numero = input("Por favor, ingrese un número positivo para calcular los factoriales: ")
# if ingreso_nat_ok(numero) == None: #Llama a la función que verifica que sea un entero positivo
#     print(f"{numero} no es un valor válido para calcular el factorial.")
# else:
#     numero = ingreso_nat_ok(numero) #Convierte el número a entero
#     for i in range (numero, 0, -1): #Recorre todos los números desde el ingreso hasta el cero
#         print(f"El factorial de {i} es {factorial_recursiva(i)}.") #Va calculando el factorial de cada valor que toma i hasta el 0


# #--------Fin del programa--------
# print("\n-----------------------Fin del Ejercicio Nº 1-----------------------\n")



# #Ejercicio N° 2
# # Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# # indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# # especifique.

# #--------Inicio del programa--------
# print("\n---------------------------Ejercicio Nº 2---------------------------\n")

# #--------Definición de funciones--------

# def sec_fibonacci(posicion): #Llamada a la función de fibonacci
#     if posicion == 0: 
#         return 0
#     elif posicion == 1:
#         return 1
#     else:
#         return sec_fibonacci(posicion-1) + sec_fibonacci(posicion-2) #Si la posición es mayor o igual a 2 retorna la suma de las últimas 2 posiciones
    
# def ingreso_nat_ok(num):
#     if not num.isdigit(): #Si no es un numero natural retorna None
#         return None
#     else:
#         return int(num) #Si es válido retorna el valor convertido de formato    


# #--------Programa principal--------

# #Solicitud de ingreso de datos

# numero = input("Por favor, ingrese una posición desde la cual se quiere obtener la secuencia de Fibonacci: ")
# if ingreso_nat_ok(numero) == None: #Llama a la función que verifica que sea un entero positivo
#     print(f"{numero} no es un valor válido para obtener la secuencia.")
# else:
#     numero = ingreso_nat_ok(numero) #Convierte el número a entero
#     for i in range (numero): #Recorre todos los números de 0 hasta la posición de la secuencia
#         print(f"La secuencia en la posición {i} es: {sec_fibonacci(i)}.") #Va retornando los valores de la posición de la secuencia


# #--------Fin del programa--------
# print("\n-----------------------Fin del Ejercicio Nº 2-----------------------\n")




# Ejercicio Nº 3
# Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1)
# Prueba esta función en un algoritmo general.

#--------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 3---------------------------\n")

#--------Definición de funciones--------

def ingreso_nat_ok(num):
    if not num.isdigit(): #Si no es un numero natural retorna None
        return None
    else:
        return int(num) #Si es válido retorna el valor convertido de formato    

def ingreso_float_ok(num):
    if (num.count('.') > 1) or (num.count('-') > 1): #Si tiene más de un punto o signo menos retorna false
        return False
    if num in ['-', '.']: #Si el valor ingresado es sólo un punto o un signo menos retorna false
        return False
    if '-' in num[1:]: #Si hay un signo menos después de la primera posición retorna false
        return False
    if '.' in num: #Si tiene un punto parte el número en 2
        parte_izq, parte_der = num.split('.')
        if parte_izq == '': #Si a la izquierda del punto no hay nada retorna false
            return False
        if parte_der == '': #Si a la derecha del punto no hay nada retorna false
            return False
        if not parte_izq.isdigit() or not parte_der.isdigit(): #Si alguna de las dos partes no es un entero retorna false
            return False
        return True #Si ambos valores a los lados del punto son enteros retorna true
    if num.startswith('-'): #Si empieza con un signo retorna la validación del is digit a partir del segundo carácter
        return num[1:].isdigit()
    return num.isdigit() #Devuelve el booleano de si es un número o no

def calculo_potencia(base, expo): # Recibe la base y el exponente
    if expo == 0: #Si el exponente es 0 retorna 1
        return 1
    else:
        return base * calculo_potencia(base, expo-1) #Multiplica al número por si mismo hasta que el exponente llegue a cero
        
#--------Programa principal--------

#Solicitud de ingreso de datos

numero = input("Por favor, ingrese un número del cual se quiere obtener la potencia: ").strip()
if ingreso_float_ok(numero): #Llama a la función que verifica que sea un flotante válido
    exponente = input(f"Por favor, ingrese un exponente para calcular la potencia de {numero}: ").strip()
    if ingreso_nat_ok(exponente) == None: #Llama a la función para verificar que el exponente sea un entero positivo válido
       print(f"{exponente} no es un exponente válido.")
    else:
        exponente = ingreso_nat_ok(exponente) #Convierte al exponente a entero
        numero = float(numero) #Se convierte el número a flotante
        print(f"{numero} elevado a la {exponente} es {calculo_potencia(numero, exponente): .2f}.") #Se llama a la función de cálculo de la potencia
else:
    print(f"{numero} no es un número válido para calcular la potencia.")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 3-----------------------\n")


# Ejercicio Nº 4
# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

#--------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 4---------------------------\n")

#--------Definición de funciones--------

def ingreso_nat_ok(num):
    if not num.isdigit(): #Si no es un numero natural retorna None
        return None
    else:
        return int(num) #Si es válido retorna el valor convertido de formato   

def convertir_a_binario(num): #Recibe el número decimal
    if num <= 1: 
        return str(num % 2) #retorna el resto de dividir por 2 en string
    else:
        return convertir_a_binario(num // 2) + str((num % 2)) #Llama a la función hasta que reste 1 o 0 y va concatenando el resto de dividir por 2 al final

#--------Programa principal--------

#Solicitud de ingreso de datos

decimal = input("Por favor, ingrese un número en base 10 para convertir a binario: ").strip()
if ingreso_nat_ok(decimal) is None: #Llama a la función para verificar si es un entero positivo 
    print(f"{decimal} no es un entero positivo válido.")
else:
    decimal = ingreso_nat_ok(decimal) #Convierte el ingreso a entero
    print(f"El número {decimal} convertido a binario es: {convertir_a_binario(decimal)}")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 4-----------------------\n")


# Ejercicio Nº 5
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

#--------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 5---------------------------\n")

#--------Definición de funciones--------


def convertir_string(palabra): #Llama a la función para reemplazar caracteres no válidos
    palabra = palabra.replace('á', 'a')
    palabra = palabra.replace('é', 'e')
    palabra = palabra.replace('í', 'i')
    palabra = palabra.replace('ó', 'o')
    palabra = palabra.replace('ú', 'u')
    palabra = palabra.replace(' ', '')
    return palabra

def es_palindromo(palabra): #Toma el string ingresado
    if len(palabra) <= 1: #Si la longitud es menor o igual a 1 se considera palíndromo
        return True
    elif palabra[0] != palabra[-1]: #Si la última letra difiere de la primera se corta la recursión
        return False
    else:
        return es_palindromo(palabra[1:-1]) #Se llama a la función nuevamente eliminando la primer y última letra
    

#--------Programa principal--------

#Solicitud de ingreso de datos

palabra = input("Ingrese una palabra para ver si es un palíndromo: ") #Verificar con "Dábale arroz a la zorra el abad"
palabra_aux =  convertir_string(palabra).strip().lower() #Se llama a la función que elimina espacios y reemplaza tildes y almacena en una variable auxiliar (para poder verificar frases)

if es_palindromo(palabra_aux):
    print(f'\n{palabra} es un palíndromo.')
else:
    print(f'\n{palabra} NO es un palíndromo.')

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 5-----------------------\n")


# Ejercicio Nº 6
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)


#--------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 6---------------------------\n")

#--------Definición de funciones--------


def ingreso_nat_ok(num):
    if not num.isdigit(): #Si no es un numero natural retorna None
        return None
    else:
        return int(num) #Si es válido retorna el valor convertido de formato
    
def suma_digitos(n): #Toma el valor ingresado
    if n // 10 == 0: #Si queda un solo dígito lo retorna
        return n
    else:
        return (n % 10) + suma_digitos(n // 10) #Va extrayendo cada dígito obteniendo el resto del módulo por 10 y llama nuevamente a la función con la división por 10 de la parte entera


#--------Programa principal--------

#Solicitud de ingreso de datos

numero = input("Por favor, ingrese un número para calcular la suma de sus dígitos: ").strip()
if ingreso_nat_ok(numero) is None: #Verifica que el número sea un entero positivo válido
    print(f"{numero} no es un entero positivo válido.")
else:
    numero = ingreso_nat_ok(numero) #Se convierte el ingreso a entero
    print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}.")


#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 6-----------------------\n")



# Ejercicio Nº 7:
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)


# --------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 7---------------------------\n")

# --------Definición de funciones--------

def ingreso_nat_ok(num):
    if not num.isdigit(): #Si no es un numero natural retorna None
        return None
    else:
        return int(num) #Si es válido retorna el valor convertido de formato
    
def contar_bloques(n): #Recibe la cantidad de bloques del nivel inferior
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1) #Va acumulando la cantidad de bloques y llama a la función nuevamente con un bloque menos hasta llegar a 1

# --------Programa principal--------

# Solicitud de ingreso de datos

bloques = input("Por favor, ingrese un número de bloques en la base para calcular cuántos necesita para toda la pirámide: ").strip()
if ingreso_nat_ok(bloques) is None or int(bloques) == 0: #Llama a la función que verifica que sea un entero positivo y verifica que haya al menos un bloque 
    print(f"{bloques} no es un número válido de bloques.")
else:   
    bloques = ingreso_nat_ok(bloques) #Se convierte el ingreso a entero
    print(f"El total de bloques necesarios para una pirámide con {bloques} bloques de base es: {contar_bloques(bloques)}.") 

# --------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 7-----------------------\n")



# Ejercicio Nº 8:
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0

# --------Inicio del programa--------

print("\n---------------------------Ejercicio Nº 8---------------------------\n")

# --------Definición de funciones--------

def ingreso_nat_ok(num):
    if not num.isdigit(): #Si no es un numero natural retorna None
        return None
    else:
        return int(num) #Si es válido retorna el valor convertido de formato

def contar_digito(numero, digito): #Recibe el número y el dígito a controlar
    if numero // 10 == 0: #Caso límite cuando la parte entera de dividir por 10 es cero
        if numero % 10 == digito: #Si el resto es igual al dígito retorna uno para contar
            return 1
        else:
            return 0
    else:
        return 1 + contar_digito((numero // 10), digito) if numero % 10 == digito else contar_digito((numero // 10), digito) 
        #Si el resto de dividir por 10 es igual al dígito ingresado va retornando uno para contar al dígito llamando a la función nuevamente con la parte entera de 
        # dividir por 10 y si no sólo vuelve hacer el llamado de esa forma, todo hasta llegar al último dígito


#--------Programa principal--------

#Solicitud de ingreso de datos

numero = input("Por favor, ingrese un número para controlar: ").strip()
if ingreso_nat_ok(numero) is None: #Llama a la función que verifica que sea un entero positivo válido
    print(f"{numero} no es un entero positivo válido.")
else:
    numero = ingreso_nat_ok(numero) #Convierte a entero al número ingresado
    digito = input(f"Por favor, ingrese un dígito para contar cuántas veces aparece en {numero}: ").strip()
    if (ingreso_nat_ok(digito) == None) or not (0 <= int(digito) <= 9): #Verifica que el dígito ingresado sea un entero válido y un dígito del 0 al 9
        print(f"{digito} no es un dígito del 0 al 9 válido.")
    else:
        digito = ingreso_nat_ok(digito) #Convierte a entero el dígito
        print(f"{digito} aparece {contar_digito(numero, digito)} veces en {numero}.")


# --------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 8-----------------------\n")