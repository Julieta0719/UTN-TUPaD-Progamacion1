#En este archivo se encuentran las funciones del Tp que se llaman en el archivo principal

#----------------------------------------------------------------------------------------------------------

#Ejercicio 1

def imprimir_hola_mundo():
    print("Hola mundo")
#----------------------------------------------------------------------------------------------------------
#Ejercicio 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!!")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 4

#Libreria math para usar el valor de PI
import math

def calcular_area_circulo(radio):
    area = float(math.pi * (radio**2))
    print(f"El área del circulo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = float(2*math.pi*radio)
    print(f"El perimetro es: {perimetro}")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 5

def segundos_a_horas(segundos):
    minutos = int(segundos//60)
    horas = int(minutos//60)
    return horas

#----------------------------------------------------------------------------------------------------------

#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero}X{i}= {numero*i}")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 7

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    print(f"La suma de los números {a} y {b} es: {suma}")
    print(f"La resta de los números {a} y {b} es: {resta}")
    print(f"La multiplicación de los números {a} y {b} es: {multiplicacion}")
    print(f"La división de los números {a} y {b} es: {division}")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 8

def calcular_imc(peso, altura):
    imc = peso//altura**2
    print(f"Su IMC es: {imc}")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    temperatura_fahrenheit = celsius * (9/5) + 32
    print(f"La temperatura de {celsius} grados celsius equivale a {temperatura_fahrenheit} grados fahrenheit")

#----------------------------------------------------------------------------------------------------------

#Ejercicio 10

def calcular_promedio(a, b, c):
    suma = int(a+b+c)
    promedio = suma//3
    print(f"El promedio de las 3 notas es: {promedio}")