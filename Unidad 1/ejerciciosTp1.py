#ejecicio1
print("Hola mundo :)")

#ejercicio2
nombre= input("Ingrese su nombre ")
print(f"Hola!, ", nombre)

#ejercicio3
nombre= input("Ingrese su nombre ")
apellido= input("Ingrese su apellido ")
edad= int(input("Cuál es su edad? "))
residencia= input("Cuál es su residencia? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#ejercicio 4
#Importamos la libreria para usar PI
import math
#Le pedimos al usuario el radio
radio= float(input("Ingrese el radio: "))
#Calculamos área y perímetro usando "math.pi" para asegurarnos de que el resultado sea más preciso
area= 2*math.pi*radio**2
perimetro= 2*math.pi*radio
print(f"El Área del círculo es: ¨{area}, y el Perímetro es: ¨{perimetro}")

#ejercicio 5
#Se le pide al usuario una cantidad de segundos
segundos= int(input("Ingrese la cantidad de segundos: "))
#Para calcular la cantidad de horas y/o minutos, dividimos los segundos por 60
horas = float = (segundos //60) //60
minutos= float = segundos //60
print(f"{segundos} segundos equivalen a: {horas} hora/s y {minutos} minuto/s")

#Ejercicio 6
#Le pedimos al usuario un número para hacer una tabla de multiplicación
numero = int(input("Ingrese un número"))
print("Tabla de multiplicación:")
print(f"{numero}X1=",numero*1)
print(f"{numero}X2=",numero*2)
print(f"{numero}X3=",numero*3)
print(f"{numero}X4=",numero*4)
print(f"{numero}X5=",numero*5)
print(f"{numero}X6=",numero*6)
print(f"{numero}X7=",numero*7)
print(f"{numero}X8=",numero*8)
print(f"{numero}X9=",numero*9)
print(f"{numero}X10=",numero*10)

#Ejercicio 7
#Se le pide al usuario dos números distintos a 0
numero1 = int(input("Ingrese un valor para el primer número, (distinto a 0): "))
numero2 = int(input("Ingrese un valor para el segundo número, (distinto a 0): "))
#Calculamos las dististas operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
#Mostramos los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#Ejercicio 8
#Se le pide al usuario ingresar su altura
altura = float(input("Ingrese su altura en metros: "))
#Pedimos que ingrese su peso
peso = int(input("Ingrese su peso en kilogramos: "))
#Calculamos el índice de masa corporal
imc = peso / altura**2
#Mostramos el resultado
print(f"Su índice de masa corporal es: {imc}")

#Ejercicio 9
#Le pedimos al usuario ingresar una temperatura en grados celsius
temperatura_celsius = int(input("Ingrese la temperatura en grados celsius: "))
#Pasamos de celsius a fahrenheit
temperatura_fahrenheit = (9/5 * temperatura_celsius) + 32
print(f"La temperatura equivalente en grados Fahrenheit es: {temperatura_fahrenheit}")

#Ejercicio 10
#Pedimos que se ingrese el valor de 3 notas para calcular su promedio
nota1 = int(input("Ingrese el valor de la primera nota: "))
nota2 = int(input("Ingrese el valor de la segunda nota: "))
nota3 = int(input("Ingrese el valor de la tercera nota: "))
#Calculamos el promedio
promedio  = (nota1 + nota2 + nota3) / 3
#Mostramos el promedio redondeado
import math
print(f"El promedio de las notas es: {math.ceil(promedio)}")
