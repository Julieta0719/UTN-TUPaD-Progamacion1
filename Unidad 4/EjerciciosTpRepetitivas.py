#Ejercicio 1

#Un mensaje que dice lo que hace el programa
print("Números enteros del 0 al 100 con estos mismos incluidos: ")

#Bucle For, para imprimir los números
for i in range(0,101,1):
    print(i)

#---------------------------------------------------------------------
#Ejercicio 2

#Pedir al usuario ingresar un número entero
numero = input("Ingrese un número entero: ")
longitud = len(numero)
print(f"El número {numero} tiene {longitud} dígito/s")

#---------------------------------------------------------------------
#Ejercicio 3

print("Se sumaran todos los números comprendidos entre dos números, excluyendo esos dos números")

#Le pedimos al usuario ingresar el valor de los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrsse el segundo número: "))

#inicializacion de variable
suma = 0

#Bucle For para sumar los números que estan entre los dos valores dados por el usuario
for i in range(numero1+1,numero2):
    suma = suma + i

#Mostramos el resultado
print(f"La suma de los números comprendidos entre {numero1} y {numero2} es: {suma}")

#---------------------------------------------------------------------
#Ejercicio 4

#Mensaje para describir lo que hace el programa
print("Ingrese [1]: para sumar números")
print("Ingrese [0]: para finalizar la suma y mostrar el total acumulado")

#Inicialización y definición de variables
suma = 0
bandera : bool = True

#Bucle while para que el usuario pueda ingresar tantos números como desee
while bandera == True:
    numero_entrada = int(input("Ingrese el número [0] o [1]: "))
    if numero_entrada == 1:
        numeros_sumar = int(input("Ingrese un número para sumar: "))
        suma = suma + numeros_sumar
    elif numero_entrada == 0:
        print(f"La suma total es: {suma}")
        print("Chauuuuuuuu")
        bandera = False
    else:
        print("Dato ingresado no es válido, debe ingresar el número [0] o [1]")

#---------------------------------------------------------------------
#Ejercicio 5

#Importamos la libreria random
import random

#Almacenamos el número aleatorio que podrá ser entre 0 y 9 incluyendolos en una variable
numero_aleatorio = random.randint(0,9)

#Definimos e inicializamos variable
bandera : bool = True
intentos = 0

#Mensaje para el usuario
print("Bienvenido a mi juego!")
print("Debe adivinar un número elegido aleatoriamente!!")
print("Tiene intentos ilimitados! Solo debe ir ingresandolos de a 1 hasta acertar. Mucha suerte!")

#Usamos un bucle while, ya que queremos que el usuario haga intentos hasta adivinar
while bandera == True:
    numero_ingresado = int(input("Ingrese un número: "))
    if numero_ingresado == numero_aleatorio:
        print(f"Felicitaciones!!! Has acertado en {intentos} intentos.")
        bandera == False
    elif numero_ingresado < 0 or numero_ingresado > 9:
        print("Debe ingresar un número entre 0 y 9")
    elif numero_ingresado != numero_aleatorio:
        print("Incorrecto, sigue intentado!")
        intentos = intentos + 1

#---------------------------------------------------------------------
#Ejercicio 6

#Mensaje para el usuario
print("A continuación se imprimirán todos los números pares comprendidos entre 100 y 0 en orden decreciente")

#Bucle for para recorrer los números
for i in range(100,0,-2):
    print(i)

#---------------------------------------------------------------------

#Ejercicio 7

#Mensaje para el usuario
print("Se sumaran todos los números comprendidos entre 0 y un número entero positivo que usted ingrese (la suma no incluye el número ingresado)")

#Inicialización de variable
bandera : bool = True
suma = 0

#Bucle while para pedir un número cuantas veces sea necesario si el usuario no ingresa un número entero positivo
while bandera == True:
    numero = (input("Ingrese un número entero positivo: "))
    if numero == "0":
        print("El número no puede ser cero")
    elif numero.isdigit():
        numero = int(numero)
        bandera = False
    else:
        print("Debe ingresar un número entero positivo")

#Bucle for para recorrer los números de 0 hasta el número dado por el usuario
for i in range(0,numero,1):
    suma = suma + i
print(suma)

#---------------------------------------------------------------------

#Ejercicio 8

#Mensaje para el usuario
print("Ingrese 100 números y se imprimirá cuantos son pares, impares, positivos y negativos")

#Inicialización de variable
contador = 0
neutro = 0
par = 0
impar = 0
positivo = 0
negativo = 0

#Bucle for para iterar del 1 al 100
for i in range(1,101):
    numeros = int(input(f"Ingrese un número, ha ingresando {contador} número/s: "))
    contador = contador + 1

     #Condicional if para comprobar si el número es par o impar
    if numeros % 2 == 0 and numeros != 0:
        par = par + 1

    if numeros % 2 != 0:
        impar = impar + 1
        
     #Condicional if para comprobar si el número es cero, positivo o negativo
    if numeros == 0:
        neutro = neutro + 1
    
    if numeros > 0 and numeros != 0:
        positivo = positivo + 1

    if numeros < 0 and numeros != 0:
        negativo = negativo + 1

#Se imprimen los resultados
print("--------------------------------------------")
print("Ha ingresado...")
print(f"Números par/es: {par}")
print(f"Números impar/es: {impar}")
print(f"Números neutro/s: {neutro}")
print(f"Números positivo/s: {positivo}")
print(f"Números negativo/s: {negativo}")

#---------------------------------------------------------------------

#Ejercicio 9

#Mensaje para el usuario
print("Ingrese 100 números para calcular su media")

#Inicialización de variable
contador = 0
suma = 0
media = 0

#Bucle for para pedir números al usuario
for i in range(1,101,1):
    numeros = int(input(f"Ingrese un número, ha ingresado {contador} números:  "))
    contador = contador + 1
    suma = suma + numeros
    media = suma // 100

print("------------------------------------------------")
print(f"La media de los números ingresados es: {media}")

#---------------------------------------------------------------------

#Ejercicio 10

#Mensaje para el usuario
print("Ingrese algún número para invertir su orden")

#Inicialización de variables
inverso = 0
negativo = ""

#Le pedimos al usuario ingresar el número
numero = int(input("Ingrese un número: "))

#Condicional if para almacenar el signo negativo en una variable auxiliar y convertir el negativo a positivo
if numero < 0:
    negativo = "-"
    numero = numero * -1

#Bucle while para invertir el número
while numero > 0:
    digito =  numero % 10
    inverso = inverso * 10 + digito
    numero = numero // 10


#Si el número es negativo la variable numero se convierte a string para agregar el signo
inverso = str(inverso)
inverso = negativo + inverso

#Se imprime el número invertido
print(f"El número invertido es: {inverso}")

