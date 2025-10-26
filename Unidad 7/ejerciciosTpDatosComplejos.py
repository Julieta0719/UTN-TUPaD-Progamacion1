#Trabajo Práctico de Datos Complejos

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 1")

#Creamos el diccionario
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

print(precios_frutas)

#Añadimos los nuevos pares key-value
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300

print(precios_frutas)

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 2")

#Actualizamos el precio de las frutas del diccionario anterior
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800

print(precios_frutas)

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 3")

#Creamos una lista con las claves del diccionario anterior
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 4")

#Creamos un diccionario vacío
contactos = {}

#Bucle for para pedir 5 pares de key-value
for i in range (1,6):
    añadir_contacto = str(input("Ingrese el nombre de la persona: ")).capitalize()
    añadir_numero = int(input(f"Ingrese el número de {añadir_contacto}: "))
    contactos[añadir_contacto] = añadir_numero

print(contactos)

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 5")

#Le pedimos una frase al usuario
frase = input("Ingrese una frase: ")

#Creamos una lista con las palabras de la frase separadas usando la función split
lista_frase = frase.split()

#Creamos un set con la lista de las palabras
set_palabras_unicas = set(lista_frase)

#Creamos un diccionario vacío
diccionario_veces_repetidas = {}

#Bucle for para contar la cantidad de veces que se repiten las palabras
for i in lista_frase:
    cantidad = lista_frase.count(i)
    diccionario_veces_repetidas [i] = cantidad

print(f"Palabras únicas: {set_palabras_unicas}")

print(f"Cantidad de veces que se repite cada palabra: {diccionario_veces_repetidas.items()} ")

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 6")

#Diccionario vacio
diccionario_alumnos = {}

#Bucle for para pedir los nombres de los alumnos
for i in range(3):
    alumno = str(input("Ingrese el nombre del alumno: ")).capitalize()

    #Lista vacia de notas
    lista_notas = []

    #Bucle for para hacer una lista de las notas
    for i in range(3):
        nota = int(input(f"Ingrese las nota del alumno {alumno}: "))
        lista_notas.append(nota)

    #Agregamos los pares key-value del diccionario con el nombre y su respectiva tupla de notas
    diccionario_alumnos [alumno] = tuple(lista_notas)
print(diccionario_alumnos)

for alumno, nota in diccionario_alumnos.items():
    suma = nota[0] + nota[1] + nota[2]
    promedio = suma // 3
    print(f"El promedio del alumno {alumno} es {promedio}")

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 7")

#Set de nombres que aprobaron el parcial 1
alumnos1 = {"Luz", "Oliver", "Alan", "Milena"}

#Set de nombres que aprobaron el parcial 2
alumnos2 = {"Luz", "Oliver","Facundo", "Fabricio"}

#Mostrar los que aprobaron ambos parciales usando la interseccion
aprobaron_ambos = alumnos1.intersection(alumnos2)
print(f"Alumnos que aprobaron ambos parciales: {aprobaron_ambos}")

print(" ")

#Mostrar los que aprobaron solo uno de los dos parciales usando la diferencia simetrica
aprobaron_uno = alumnos1.symmetric_difference(alumnos2)
print(f"Alumnos que aprobaron solo uno de los dos parciales: {aprobaron_uno}")

print(" ")

#Solo los que aprobaron el 1 parcial:
print(f"Alumnos que aprobaron el primer parcial: {alumnos1}")

print(" ")

#Solo los que aprobaron el 2 parcial:
print(f"Alumnos que aprobaron el segundo parcial: {alumnos2}")

print(" ")

#Mostar los aprobaron almenos un parcial sin repetir usando la union
aprobaron_alguno = alumnos1.union(alumnos2)
print(f"Alumnos que aprobaron al menos uno de los parciales: {aprobaron_alguno}")

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 8")

#Inicializacion de diccionario
diccionario_productos = {}

#Bandera para las opciones interactivas
bandera: bool = True

#Condicional para que el usuario llene el diccionario
if not diccionario_productos:
    for i in range (3):
        clave_producto = input("Ingrese el nombre del producto que desea añadir: ").capitalize()
        valor_stock = int(input(f"Ingrese el número de la cantidad disponible del producto {clave_producto}: "))
        diccionario_productos[clave_producto] = valor_stock

#Bucle while para el menu de las opciones interactivas
while bandera == True:
    print("Bienvenido al menú de productos, a continuación se le mostrarán las opciones interactivas")
    print(" ")
    print("[1]: Consultar el stock de un producto ingresado")
    print("[2]: Agregar unidades al stock si el producto ya existe")
    print("[3]: Agregar un nuevo producto si no existe")
    print("[4]: Salir")
    print(" ")

    opcion = input("Ingrese el número de la opción con la que desea interactuar: ")
    if opcion.isdigit():
        opcion = int(opcion)

        if opcion >= 1 and opcion <= 4:

            #Opcion 1
            if opcion == 1:
                producto_ingresado = input("Ingrese el nombre del producto del que desea consultar su stock: ").capitalize()
                if producto_ingresado in diccionario_productos:
                    print(f"{producto_ingresado}: {diccionario_productos[producto_ingresado]}")
                else:
                    print("El producto que se ingreso no se encuentra en el diccionario")
            #Opcion 2
            elif opcion == 2:
                actualizar_stock = input("Ingrese el nombre del producto del que desee agregar stock: ").capitalize()
                if actualizar_stock in diccionario_productos:
                    cantidad_agregar = int(input("Ingrese el número de la cantidad que desea agregar al stock: "))
                    diccionario_productos[actualizar_stock] += cantidad_agregar
                else:
                    print("El producto no se encuentra en el diccionario")

            #Opcion 3
            elif opcion == 3:
                agregar_producto = input("Ingrese el nombre del producto que desee agregar añ diccionario: ").capitalize()
                if not agregar_producto in diccionario_productos:
                    cantidad_stock = int(input("Ingrese el número de la cantidad de stock disponible: "))
                    diccionario_productos[agregar_producto] = cantidad_stock
                else:
                    print("El producto ingresado ya está en en el diccionario")
            #Opcion 4
            elif opcion == 4:
                print("Saliendo...")
                bandera = False
            else:
                print("La opción ingresada no es valida")
        else:
            print("Incorrecto, debe ingresar un número entre 1 y 4")
    else:
        print("Incorrecto, debe ingresar un número")

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 9")

#Diccionario con la agenda donde las key son (día, hora) y los value son actividades
diccionario_agenda = {("Lunes", "14:45"): "Clase de arquitectura", ("Martes", "20:00"): "Salir a comprar", ("Miercoles", "14:30"): "Parcial de programción"}

#Le mostramos al usuario los días y horas anotadas en la agenda
print(f"Días y horas agendadas: {list(diccionario_agenda.keys())}")

print(" ")

#Pedimos el día y hora
dia = input("Ingrese el dia de cual desea ver su actividad agendada: ").capitalize()
hora = input("Ingrese la hora: ")
tupla_consultar_actividad = (dia, hora)

#Condicional para comprobar si el día y la hora son correctas, y se muestra su actividad agendada
if tupla_consultar_actividad in diccionario_agenda:
    print(f"La actividad del día y hora {tupla_consultar_actividad} es {diccionario_agenda[tupla_consultar_actividad]}")
else:
    print("El día o la fecha ingresados son incorrectos, por favor intente nuevamente")

print("-------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 10")

#Diccionario con claves de países y valores de su respectiva capital
diccionario_paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Francia": "Paris"}

#Diccionario vacio donde se guardara el invertido
diccionario_invertido = {}

#Bucle for para reccorer el diccionario original y guardar sus pares key-value en dos variables auxiliares y guardarlas en el nuevo diccionario
for clave, valor in diccionario_paises.items():
    nuevo_valor = clave
    nueva_clave = valor

    diccionario_invertido[nueva_clave] = nuevo_valor

print(f"Diccionario original: {diccionario_paises}")
print(f"Diccionario invertido: {diccionario_invertido}")

