#---------------------------------------------------PRÁCTICA Nº 7--------------------------------------------------#
#--------------------------------------------------DATOS COMPLEJOS-------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#


# #Ejercicio N° 1
# # Dado el diccionario precios_frutas
# # precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# # Añadir las siguientes frutas con sus respectivos precios:
# # ● Naranja = 1200
# # ● Manzana = 1500
# # ● Pera = 2300

# #--------Inicio del programa--------
# print("\n---------------------------Ejercicio Nº 1---------------------------\n")

# #--------Programa principal--------

# # Declaración del diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# #Incorporación de las nuevas frutas y precios
# precios_frutas.update({'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300})

# #Muestra del diccionario actualizado
# print(precios_frutas)

# #--------Fin del programa--------
# print("\n-----------------------Fin del Ejercicio Nº 1-----------------------\n")



# #Ejercicio N° 2
# # Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# # ● Banana = 1330
# # ● Manzana = 1700
# # ● Melón = 2800

# #--------Inicio del programa--------
# print("\n---------------------------Ejercicio Nº 2---------------------------\n")

# #--------Programa principal--------

# #Actualización de los precios de las frutas seleccionadas
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# #Muestra del diccionario actualizado
# print(precios_frutas)

# #--------Fin del programa--------
# print("\n-----------------------Fin del Ejercicio Nº 2-----------------------\n")

# #Ejercicio N° 3
# # Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# # precios.

# #--------Inicio del programa--------
# print("\n---------------------------Ejercicio Nº 3---------------------------\n")

# #--------Programa principal--------

# #Se extraen las keys del diccionario, se las convierte a lista y se las almacena en una nueva variable
# lista_frutas = list(precios_frutas.keys())

# #Salida de datos
# print(lista_frutas)

# #--------Fin del programa--------
# print("\n-----------------------Fin del Ejercicio Nº 3-----------------------\n")


#Ejercicio N° 4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

#--------Inicio del programa--------
print("\n---------------------------Ejercicio Nº 4---------------------------\n")

def telefono_valido(numero):
    if numero.isdigit(): #Se verifica que la cantidad sea un entero válido (no admite negativos ni flotantes)
        if len(numero) > 6 and len(numero) < 15: #Se verifica que sea de una longitud adecuada
            numero = int(numero) #Se convierte el numero a entero
            return numero #Se devuelve el número convertido
        else:
            return False #Si no cumple se devuelve falso
    else:
        return False #Si no cumple se devuelve falso


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

while True:
    nombre = input(f"\nPor favor, ingrese el nombre de un contacto: ").title()
    if nombre in contactos: #Si el contacto está en la agenda se muestra el teléfono
        print(f"El teléfono de {nombre} es: {contactos[nombre]}.")
    else:
        print(f"{nombre} no está agendado.")
    seguir = input("\n¿Desea ver otro número? (S/N): ").capitalize()
    if seguir == "S":
        continue
    elif seguir == "N":
        break
    else:
        print("Valor incorrecto.")

#--------Fin del programa--------
print("\n-----------------------Fin del Ejercicio Nº 4-----------------------\n")


