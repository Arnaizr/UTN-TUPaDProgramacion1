#--------------Práctica Nº 4--------------#
#---------Estructuras Repetitivas---------#

# #Ejercicio Nº 1
# # 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# #Inicio de programa
# print ("Ejercicio Nº 1")
# #Inicio de bucle de repetición incondicional
# for i in range (101): #Se establece el rango hasta 101 dado que es excluyente
#     print (i)
# #Fin del bucle
# #Fin del programa

# #Ejercicio Nº 2
# # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# # dígitos que contiene.

# #Inicio de programa
# print ("Ejercicio Nº 2")
# # Solicitud de ingreso de datos
# numero = int(input("Hola, por favor ingrese un número entero: "))
# #Inicialización de variable contador
# if numero == 0:
#     cont = 1 #Se inicializa como 1 ya que nunca entrará al bucle
# else:
#     cont = 0 #En el caso contrario se inicializa como 0 para contar dígitos en el bucle
# #Inicialización del bucle que cuenta la cantidad de dígitos del número ingresado
# while numero != 0: #Sale del bucle si no quedan más dígitos que extraer
#     numero = int(numero/10) #Va extrayendo los dígitos del número ingresado de uno en uno
#     cont += 1 #incrementa el contador por cada bucle (y por cada dígito extraído)
# #Fin del bucle
# #Salida de datos
# print (f"La cantidad de dígitos del número ingresado es: {cont}.")
# #Fin del programa

# #Ejercicio Nº 3
# # 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# # dados por el usuario, excluyendo esos dos valores.

# #Inicio del programa
# print ("Ejercicio Nº 3")
# #Solicitud de ingreso de datos
# num1 = int(input("Hola, por favor ingrese un número entero: "))
# num2 = int(input("Hola, por favor ingrese otro número entero: "))
# #Inicio de estructura condicional para verificar qué numero es el mayor
# if num1 > num2:
#     mayor = num1
#     menor = num2
# else:
#     mayor = num2
#     menor = num1
# #Fin de estrucura condicional
# #Inicio de estructura condicional para verificar si los números son consecutivos o iguales (bucle infinito)
# if (mayor-menor) <= 1:
#     print(f"Los números {num1} y {num2} son consecutivos o iguales, no hay números comprendidos entre ellos.")
# else:
#     suma = 0 #Inicialización de la variable que acumula la sumatoria de los números intermedios.
#     #Inicialización del bucle que va de los números comprendidos entre los números ingresados
#     for i in range (menor+1, mayor):
#         suma += i #acumula todos los valores que toma i
#     #Fin del bucle
#     #Salida de datos
#     print(f"La sumatoria de los números comprendidos entre {num1} y {num2} es: {suma}.")
# #Fin del condicional
# #Fin del programa

# #Ejecricio Nº 4
# # 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# # secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# # un 0.

# #Inicio del programa
# print("Ejercicio Nº 4:")
# #Inicialización de variable acumuladora
# suma = 0
# #Ingreso de datos
# num = int(input("Hola, por favor ingrese un número para empezar a contar: "))
# #Inicio del bucle acumulador de numeros ingresados
# while num != 0:
#     suma += num #Incrementa el acumulador con los números ingresados
#     #Solicitud de un nuevo número
#     num = int(input("Por favor ingresar un nuevo número para contar o salir con cero: "))
# #Fin del bucle
# #Salida de datos
# print(f"La sumatoria de los números ingresados es: {suma}.")
# #Fin del programa