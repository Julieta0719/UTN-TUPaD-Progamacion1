#Ejercicio 1
#Se le pide al usuario su edad
edad = int(input("Ingrese su edad: "))
#Si tiene entre 18 y 80 se muestra el mensaje "Es mayor de edad"
if edad >= 18 and edad <= 80:
    print("Es mayor de edad")
#Si tiene entre 0 y 17 se muestra el mensaje "Es menor de edad"
elif edad < 18 and edad >= 0:
    print("Es menor de edad")
#De otro modo se mostrará el mensaje "El número no es válido"
else:
    print("El número no es válido")

#Ejercicio 2
#Pedimos al usuario ingresar su nota
nota = int(input("Ingrese la nota: "))
#Si la nota es mayor o igual a 6 se muestra el mensaje "Aprobado"
if nota >= 6:
    print("Aprobado")
#Si la nota es menor a 6 se muestra el mensaje "Desaprobado"
else:
    nota < 6 and nota >= 0
    print("Desaprobado")

#Ejercicio 3
numero_ingresado = int(input("Ingrese un número par: "))
#En el caso que el número sea cero se mostrará el mensaje "El número es 0"
if numero_ingresado == 0:
    print("El número es 0")
#Si el usuario ingresa un número par se muestra muestra el mensaje "Ha ingresado un número par"
elif numero_ingresado % 2 == 0:
    print("Ha ingresado un número par")
#Si se ingresa un número impar se muestra el mensaje "Por favor, ingrese un número par"
else:
     print("Por favor, ingrese un número par")

#Ejercicio 4
#Se le pide al usuario ingresar su edad
edad = int(input("Cuál es su edad?: "))
#Verificamos su categoria dependiendo de la edad ingresada
if edad < 12 and edad >= 0:
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres adolescnete")
elif edad >= 18 and edad < 30:
    print("Eres adulto/a joven")
elif edad >= 30 and edad <= 65:
    print("Eres adulto/a")
else:
    print("El número ingresado no es válido")

#Ejercicio 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud = len(contraseña)
print(longitud)
if longitud <= 8 or longitud >= 14:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")

#Ejercicio 6
import random
#lista de números aleatorios
numeros = [random.randint(1,100) for i in range(50)]

#llamado del paquete statistics y las funciones "moda, media y promedio"
from statistics import mode, median, mean

#hacer uso de las funciones con la lista de números aleatorios
moda = mode(numeros)
print("La moda es: ", moda)
mediana = median(numeros)
print("La mediana es: ", mediana)
media = mean(numeros)
print("La media es: ", media)

#compararlas para determinar si su sesgo es positivo, negativo o no hay sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("La lista aleatoria no cumple con ninguna de las condiciones del sesgo")

#Ejercicio 7
#Pedirle al usuario el ingreso de una palabra o frase
palabra = str(input("Ingrese una palabra o frase: ")).lower()

#calcular la longitud para luego obtener la última letra de la palabra o frase
longitud = len(palabra)
ultima_letra = palabra[longitud -1]

#Evaluamos si la letra es una vocal o no
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{palabra}!")
else:
    print(palabra)

#Ejercicio 8
#Solicitamos el nombre del usuario
nombre = str(input("Ingrese su nombre: "))

#Le pedimos que ingrese un número del 1 al 3
print("[1]: Si quiere su nombre en mayúsculas")
print("[2]: Si quiere su nombre en minúsculas")
print("[3]: Si quiere su nombre con la primera letra en mayúscula")
numero = int(input("Ingrese un número: "))

#Condiciones dependiendo del número ingresado
if numero == 1:
    nombre_mayusculas = nombre.upper()
    print(f"Hola! {nombre_mayusculas}")
elif numero == 2:
    nombre_minusculas = nombre.lower()
    print(f"Hola! {nombre_minusculas}")
elif numero == 3:
    nombre_mayus_minus = nombre.capitalize()
    print(f"Hola! {nombre_mayus_minus}")
else:
    print(f"El número {numero} no es válido")

#Ejercicio 9
#Solicitamos el número de la magnitud
magnitud = int(input("Ingrese la magnitud del terremoto: "))

#Condicional if para comprobar su categoria
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

#Ejercicio 10
#Le preguntamos al usuario en que hemisferio se encuentra (Norte/Sur)
hemisferio = str(input("Ingrese el hemisferio en el que se encuentra [N/S]: ")).upper()

#Preguntamos el mes del año
mes = str(input("Ingrese el nombre del mes actual: ")).upper()

#Preguntamos el día
dia = int(input("Ingrese el número del día: "))

if hemisferio == "N":
    if (mes == "DICIEMBRE" and dia > 21)  or (mes == "ENERO") or (mes == "FEBRERO") or (mes == "MARZO" and dia <= 20):
        print("Invierno")
    elif  (mes == "MARZO" and dia > 21)  or (mes == "ABRIL") or (mes == "MAYO") or (mes == "JUNIO" and dia <= 20):
        print("Primavera")
    elif (mes == "JUNIO" and dia > 21)  or (mes == "JULIO") or (mes == "AGOSTO") or (mes == "SEPTIEMBRE" and dia <= 20):
        print("Vernao")
    elif (mes == "SEPTIEMBRE" and dia > 21)  or (mes == "OCTUBRE") or (mes == "NOVIEMBRE") or (mes == "DICIEMBRE" and dia <= 20):
        print("Otoño")
elif hemisferio == "S":
    if (mes == "DICIEMBRE" and dia > 21)  or (mes == "ENERO") or (mes == "FEBRERO") or (mes == "MARZO" and dia <= 20):
        print("Verano")
    elif  (mes == "MARZO" and dia > 21)  or (mes == "ABRIL") or (mes == "MAYO") or (mes == "JUNIO" and dia <= 20):
        print("Otoño")
    elif (mes == "JUNIO" and dia > 21)  or (mes == "JULIO") or (mes == "AGOSTO") or (mes == "SEPTIEMBRE" and dia <= 20):
        print("Invierno")
    elif (mes == "SEPTIEMBRE" and dia > 21)  or (mes == "OCTUBRE") or (mes == "NOVIEMBRE") or (mes == "DICIEMBRE" and dia <= 20):
        print("Primavera")
        