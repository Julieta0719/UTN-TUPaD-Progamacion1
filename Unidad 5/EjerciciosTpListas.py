#Ejercicio 1

#Mensaje para el usuario
print("Lista del 1 al 100 de números múltiplos de 4")

#Creamos una lista vacía donde se almacenarán los múltiplos de 4
lista_multiplos_4 = []

#Bucle for para encontar y almacenar los  múltiplos de 4 en la lista vacía
for i in range(1,101):
    if i % 4 == 0:
        lista_multiplos_4.append(i)

#Imprimimos la lista
print(f"Lista con elementos múltiplos de 4: {lista_multiplos_4}")

#-------------------------------------------------------------------------

#Ejercicio 2

#Mensaje para el usuario
print("Se imprimirá el penúltimo elemento de la siguiente lista: ")

#Creamos lista de cinco elementos y la imprimimos
lista_juegos = ["Dead By Daylight", "Left 4 Dead", "Red Dead Redemption", "Team Fortress", "Bioshock" ]
print(lista_juegos)

#Guardamos el penúltimo elemento en una variable
indice_lista = lista_juegos[3]

#Imprimimos el penúltimo elemento
print(indice_lista)

#-------------------------------------------------------------------------

#Ejercicio 3

#Mensaje para el usuario
print("Se creó una lista vacía, ingrese 3 palabras de a 1 para llenar la lista")

#Creamos la lista
lista_vacia = []

for i in range(0,3):
    #Pedimos al usuario ingresar los elementos para añadir a la lista
    elemento = input("Ingrese una palabra: ")
    #Se añaden los elementos a la lista vacía
    lista_vacia.append(elemento)

#Se imprime la lista
print(lista_vacia)

#-------------------------------------------------------------------------

#Ejercicio 4

#Mensaje para el usuario
print("Se imprimirá una lista de animales y se remplazará tanto el segundo como el último elemento de la lista por las palabras 'loro' y 'oso': ")

#Lista de animales
lista_animales = ["perro", "gato", "conejo", "pez"]
print(lista_animales)

#Modificación de los elementos de la lista
lista_animales[1] = "loro"
lista_animales[3] = "oso"

#Se imprime la lista nueva
print("----------------------------------------------------")
print("Lista modificada: ")
print(lista_animales)

#-------------------------------------------------------------------------

#Ejercicio 5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

"""""
Por lo que veo se crea una lista de numeros que contiene 5 elementos y se utliza la función remove para eliminar un elemento
y al parecer al usar la palabra 'max' entre paréntesis después del .remove() y antes del nombre de la lista se ve que lo que hace es
eliminar el elemento más grande de la lista de números que en este caso es el 22, ya que al imprimir la lista se ven 4 elementos y
el que falta es el más grande de esos 4. Por lo tanto en conclusión el programa elimina el elemento más grande de la lista e imprime la lista
modificada.
"""""
#-------------------------------------------------------------------------

#Ejercicio 6

#Mensaje para el usuario
print("Se creó una lista de números del 10 al 30 incluído, con saltos de 5 en 5")
print("Se imprimirán los 2 primeros números: ")

#Creación de la lista
lista_numeros = list(range(10,31,5))
print(lista_numeros[0], " ", lista_numeros[1])

#-------------------------------------------------------------------------

#Ejercicio 7

print("Lista de autos")

autos = ["sedan", "polo", "suran", "gol"]
print(autos)

print("A continuación deberá modificar los elementos de los índices 1 y 2")

#Bucle for para pedir 2 veces que se ingrese un dato
for i in range(1,3):
    nuevo_elemento = input("Ingrese un nuevo elemento para modificar la lista: ")

    #Sobreescribimos los elementos de la lista en los índices 1 y 2 con los datos ingresados por el usuario
    autos[1] = nuevo_elemento
    autos[2] = nuevo_elemento

print("Lista modificada: ")
print(autos)

#-------------------------------------------------------------------------

#Ejercicio 8

#Lista vacía
dobles = []

#Agregar el doble de 5, 10 y 15 usando .append()
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

#Imprimir la lista
print(dobles)

#-------------------------------------------------------------------------

#Ejercicio 9

print("Lista de compras inicial: ")
#Lista de compras de los 3 clientes diferentes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]


#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")


#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"


#c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")


#d) Imprimir la lista resultante por pantalla
print("----------------------------------------------")
print("Lista de compras final: ")
print(compras)

#-------------------------------------------------------------------------

#Ejercicio 10

print("Lista anidada: ")

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

#Imprimir la lista resultante por pantalla
print(lista_anidada)