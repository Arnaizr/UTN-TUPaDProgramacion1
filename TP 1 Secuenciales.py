#Ejercicio 1
print("Ejercicio 1:")
print("Hola mundo!\n\n")

#Ejercicio 2
print("Ejercicio 2:")
#Ingreso de valores
nombre = input("Ingrese el nombre del usuario: ")
#Saludo al usuario
print(f"Hola {nombre}!\n\n")

#Ejercicio 3
print("Ejercicio 3:")
#Ingreso de valores
nombre = input("Ingrese el nombre del usuario: ")
apellido = input("Ingrese el apellido del usuario: ")
edad = int(input("Ingrese la edad del usuario: "))
residencia = input("Ingrese el lugar de residencia del usuario: ")
#Mensaje de presentación del usuario
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.\n\n")

#Ejercicio 4
print("Ejercicio 4:")
#Ingreso de valores
radio = float(input("Ingresar el radio de un círculo: "))
pi =  3.14159
#Cálculo de las medidas del círculo
area = pi*(radio**2)
longitud = 2*pi*radio
#Devolución de las medidas
print(f"Un círculo con un radio de {radio} tiene un área de  {area} y una longitud de la circunferencia de {longitud}.\n\n")

#Ejercicio 5
print("Ejercicio 5:")
#Ingreso de valores
segundos = int(input("Ingresar segundos para convertir a horas: "))
#Cálculo valores
minutos =  segundos // 60 #Se calcula a cuántos minutos enteros equivalen los segundos ingresados
segunaux = segundos % 60 #Se calcula el resto de los segundos que quedarían y almacenan en una variable auxiliar
horas = minutos // 60 #Se calcula a cuántas horas enteras equivalen los minutos calculados
minutos = minutos % 60 #Se reemplazan el total de minutos por los minutos restantes del cálculo de horas
#Devolución de los valores
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segunaux} segundos.\n\n")

#Ejercicio 6
print("Ejercicio 6: ")
#Ingreso de valores
num = int(input("Ingrese un número: "))
#Devolución de la tabla de multiplicar
print(f"La tabla de multiplicar de {num} es: \n{num*1}\n{num*2}\n{num*3}\n{num*4}\n{num*5}\n{num*6}\n{num*7}\n{num*8}\n{num*9}\n{num*10}\n\n")

#Ejercicio 7
print("Ejercicio 7: ")
#Ingreso de valores
num1 = int(input("Ingrese el primer número para operar (distinto de cero): "))
num2 = int(input("Ingrese el segundo número para operar (distinto de cero): "))
#Cálculo de las operaciones solicitadas
suma = num1+num2
resta = num1-num2
producto = num1*num2
division = num1/num2
#Devolución de las operaciones
print(f"El resultado de las operaciones entre {num1} y {num2} es:\nSuma: {suma}\nResta: {resta}\nProducto: {producto}\nDivisión: {division}\n\n")

#Ejercicio 8
print("Ejercicio 8: ")
#Ingreso de valores
peso = float(input("Ingrese el peso del usuario (en kilogramos): "))
altura = float(input("Ingrese la altura del usuario (en metros): "))
#Cálculo y devolución del índice de masa corporal
IMC = peso/(altura**2)  
print(f"El índice de masa corporal del usuario es {IMC}.\n\n")

#Ejercicio 9
print("Ejercicio 9: ")
#Ingreso de valores
celsius = float(input("Ingrese una temperatura en grados celsius: "))
#Cálculo y devolución de la temperatura en farenheit
farenheit = 9/5*(celsius)+32  
print(f"{celsius} °C equivalen a {farenheit} °F.\n\n")

#Ejercicio 10
print("Ejercicio 10: ")
#Ingreso de valores
A = int(input("Ingrese el primer número: "))
B = int(input("Ingrese el segundo número: "))
C = int(input("Ingrese el tercer número: "))
#Cálculo del promedio
promedio = (A+B+C)/3
#Devolución de resultados
print(f"El promedio de {A}, {B} y {C} es: {promedio}.\n\n")