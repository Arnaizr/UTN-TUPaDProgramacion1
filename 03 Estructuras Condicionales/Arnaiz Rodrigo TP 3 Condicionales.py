#--------------Práctica Nº 3--------------#
#--------Estructuras Condicionales--------#

#Ejercicio Nº 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# #Inicio de programa
# print("Ejercicio 1:")
# #Carga de datos
# edad = int(input("Hola, por favor ingrese la edad del usuario: "))
# #Inicio de estructura condicional para verificar si el usuario es mayor de edad
# if edad >= 18:
#     #Salida de información
#     print("Es mayor de edad")
# #Fin de estructura condicional
# #Fin del programa

# Ejercicio Nº 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”
# Inicio de programa

# print("Ejercicio 2:")
# #Carga de datos
# nota = float(input("Hola, por favor ingresar la nota del usuario: "))
# #Inicio de estructura condicional para verificar la condición de aprobado
# if nota >= 6:
#     #Salida de información
#     print("Aprobado.")
# #else:
#     print("Desaprobado.")
# #Fin de estructura condicional
# #Fin de programa

#Ejercicio Nº 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

# #Inicio de programa
# print("Ejercicio 3:")
# #Carga de datos
# num = int(input("Hola, por favor ingresar un número par: "))
# #Procesamiento de datos
# resto = num % 2 #Se verifica que el resto de la división por dos sea cero
# #Inicio de estructura condicional para verificar si el número es par
# if resto == 0:
#     #Salida de información
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")
# #Fin de estructura condicional
# #Fin del programa

#Ejercicio Nº 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# #Inicio de programa
# print("Ejercicio 4:")
# #Carga de datos
# edad = int(input("Hola, por favor ingresar la edad del usuario: "))
# #Inicio de la estructura condicional para determinar la franja etaria con devolución de información
# if edad >= 0 and edad < 12:
#     print("El usuario es un/a niño/a.")
# elif edad >= 12 and edad < 18:
#     print("El usuario es un/a adolescente.")
# elif edad >= 18 and edad < 30:
#     print("El usuario es un/a adulto/a joven.")
# elif edad >= 30 and edad <= 120:
#     print("El usuario es un/a adulto.") #Se determina un valor máximo de 120 años
# else:
#     print("La edad ingresada no es válida.") #Se muestra este mensaje si se ingresa un valor menor a cero o mayor a 120.
# #Fin del condicional
# #Fin del Programa

# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# #Inicio de programa
# print("Ejercicio 5:")
# #Carga de datos
# contrasenia = str(input("Hola, por favor ingrese una contraseña entre 8 y 14 caracteres: "))
# #Cálculo de longitud de la contraseña
# longitud = len(contrasenia)
# #Inicio de la estructura condicional para determinar si la contraseña es adecuada con devolución de información
# if longitud >= 8 and longitud <= 14:
#     print("Ha ingresado una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
# #Fin del condicional
# #Fin del programa