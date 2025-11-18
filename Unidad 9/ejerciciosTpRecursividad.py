print("Trabajo Práctico de Recursividad")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 1")
print("")

#Funcion para calcular el factorial de un número
def factorial(num):
    #Caso base
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

num = int(input("Ingrese un número entero positivo para calcular su factorial: "))

#Imprimir los factoriales desde 1 hasta el número ingresado
print("")
print(f"--Factoriales desde 1 hasta {num}--")
for i in range(1,num +1):
    print(f"{i}!: {factorial(i)}")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 2")
print("")

#Funcion para calcular fibonacci
def fibonacci(num):
    #caso base
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num -2)


posicion= int(input("Ingrese el número de la posición, debe ser entero y positivo: "))

#Imprimir la serie de fibonacci hasta la posición ingresada
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion +1):
    print(f"{i} = {fibonacci(i)}")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 3")
print("")

#Funcion para calcular la potencia
def potencia(base, exponente):
    #caso base
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente al que desea elevar la base: "))

#Imprimir el resultado
print(f"{base}**{exponente} =  {potencia(base, exponente)}")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 4")
print("")

def convertir_decimal_a_binario (decimal):
    #caso base
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        cociente = decimal // 2
        resto = decimal % 2
        #se retorna el resto como string para que se devuelva una cadena de texto y se sume el digito a la cadena
        return convertir_decimal_a_binario(cociente) + str(resto)

print("---Conversor de decimal a binario---")
decimal = int(input("Ingrese el número decimal que desea convertir a binario: "))
print(f"{decimal} (decimal) = {convertir_decimal_a_binario(decimal)} (binario) ")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 5")
print("")

def es_palindromo(palabra):
    #caso base
    if len(palabra) <= 1:
        return True

        #comparamos la primer y última letra, y si no son iguales se retorna false y finaliza la función
    if palabra[0] != palabra[-1]:
        return False
    
    else:
        #quitamos la primer y última letra, para seguir comparando el resto de la cadena
        return es_palindromo(palabra[1:-1])



palabra = input("Ingrese una palabra para evaluar si es un polindromo: ").lower()

#Validamos que no hayan tildes
tildes = "ÁÉÍÓÚáéíóú"

tiene_tilde: bool = False

for letra in palabra:
    if letra in tildes:
        tiene_tilde = True
        break


#Validamos que la palabra solo contenga letras y no tenga espacios
if (palabra.isalpha()) and (palabra.strip() != " ") and (tiene_tilde == False):
    str(palabra)
    retorno = es_palindromo(palabra)
    print(retorno)

else:
    print("La palabra no debe tener espacios ni tildes")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 6")
print("")

def suma_digitos(num):
    #caso base
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)

num = int(input("Ingrese un número entero positivo para sumar sus digitos: "))

suma = suma_digitos(num)

print(f"La suma de los digitos es: {suma}")


print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 7")
print("")

def contar_bloques(num):
    #caso base
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        bloques = num + contar_bloques(num -1)
        return bloques


nivel_bajo = int(input("Ingrese la cantidad de bloques del nivel más bajo de la pirámide: "))

cant_bloques = contar_bloques(nivel_bajo)
print(f"La cantidad de bloques requeridos para armar la pirámide es de: {cant_bloques}")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Ejercicio 8")
print("")

def contar_digito(numero, digito):
    #caso base
    if numero == "":
        return 0

    contador = 0
    if numero[0] == digito:
        contador = contador + 1

    return contador + contar_digito(numero[1:], digito)


numero = (input("Ingrese 1 o más números: "))
digito = (input("Ingrese el número de un dígito: "))

cantidad = contar_digito(numero, digito)

print(f"El digito {digito} aparece {cantidad} veces en [{numero}]")