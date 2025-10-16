#Tp de Funciones

print("Ejercicio 1")

"""""""""
Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal
"""""""""
#importamos la función desde el archivo de funciones
from funciones import imprimir_hola_mundo

#llamado de la función
imprimir_hola_mundo()

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 2")

"""""""""
Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario
"""""""""
#importación de la función
from funciones import saludar_usuario

#se le pide al usuario el nombre y se le envía el argumento a la función
nombre = input("Saludos, ingrese su nombre: ").capitalize()
saludar_usuario(nombre)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 3")

"""""""""
Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
“Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con
los valores ingresados
"""""""""

from funciones import informacion_personal

#Le pedimos los datos al usuario
nombre = str(input("Ingrese su nombre: ")).capitalize()
apellido = str(input("Ingrese su apellido: ")).capitalize()
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese el nombre de su residencia: ")).capitalize()

#Le enviamos los argumentos a la función
informacion_personal(nombre, apellido, edad, residencia)
print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 4")

"""""""""
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""""""""

from funciones import calcular_area_circulo, calcular_perimetro_circulo

#Pedimos el radio
radio = int(input("Ingrese el radio del circulo: "))

#Le enviamos los argumentos a las funciones
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 5")

"""""""""
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""""""""
from funciones import segundos_a_horas

#Le pedimos al usuario la cantidad de segundos
segundos= int(input("Ingrese la cantidad de segundos: "))

#Enviamos el argumento a la función
horas = segundos_a_horas(segundos)
print(f"La cantidad de {segundos} segundo/s es equivalente a {horas} hora/s")

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 6")

"""""""""
Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función
"""""""""

from funciones import tabla_multiplicar

#Le pedimos al usuario el número del que se va a mostrar su tabla
numero = int(input("Ingrese un número: "))

#Le enviamos el argumento a la función
print(f"Tabla de multiplicar del número {numero}")
tabla_multiplicar(numero)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 7")

"""""""""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""""""""

from funciones import operaciones_basicas

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#enviamos los argumentos
operaciones_basicas(num1, num2)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 8")

"""""""""
Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
y devuelva el índice de masa corporal (IMC).
Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""""""""

from funciones import calcular_imc

#Le pedimos al usuario los datos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

#enviamos los argumentos
calcular_imc(peso, altura)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 9")

"""""""""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función
"""""""""

from funciones import celsius_a_fahrenheit

#Le pedimos al usuario los grados celsius
temperatura_celsius = int(input("Ingrese la temperatura en celsius: "))

#enviamos el argumento a la función
celsius_a_fahrenheit(temperatura_celsius)

print("-------------------------------------------------------------------------------------------------------")

print("Ejercicio 10")

"""""""""
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""""""""

from funciones import calcular_promedio

#Pedimos las notas
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

#Enviamos los argumentos
calcular_promedio(nota1, nota2, nota3)