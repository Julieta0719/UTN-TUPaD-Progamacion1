#Trabajo Práctico de Manejo de Archivos

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 1")

#Creación del archivo txt usando el metodo with
with open("productos.txt", "w") as archivo:
    archivo.write("Gabinete, 5000, 2\n")
    archivo.write("Monitor, 2000, 5\n")
    archivo.write("Teclado, 1300, 7\n")

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 2")

#Bloque with para abrir en archivo productos.txt para lectura
with open("productos.txt", "r") as archivo:

    #Bucle for para leer linea por linea
    for linea in archivo:
        producto, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")
        print(" ")

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 3")

#Bloque with para abrir el archivo productos.txt para agregar datos
with open ("productos.txt", "a") as archivo:

    #Pedimos los datos al usuario
    nuevo_producto = input("Ingrese el nombre del producto que desea añadir: ").capitalize()
    precio = input(f"Ingrese el precio del producto que desea añadir {nuevo_producto}: ")
    cantidad = input(f"Ingrese el número de la cantidad de stock del producto {nuevo_producto}: ")
    
    #f-string para añadir los datos ingresados a una línea nueva del archivo productos.txt
    nueva_linea = f"{nuevo_producto}, {precio}, {cantidad}\n"
    archivo.write(nueva_linea)

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 4")

#Bloque with para leer el archivo productos.txt linea por linea
with open("productos.txt", "r") as archivo:
    for linea in archivo:

        #Funcion strip para eliminar saltos de linea o espacios vacios
        linea = linea.strip()

        #Funcion split para separar los datos con comas, (se genera una lista donde cada string es un elemento)
        lista_datos_separados = linea.split(",")

        #Asignamos los datos de cada linea a las variables que seran los valores del diccionario
        #Teniendo en cuenta que en cada fila el indice[0] tiene el nombre del producto, indice[1] el precio, y indice[2] la cantidad
        #Funcion strip para eliminar los espacios en blanco al principio y al final de cada string
        producto = lista_datos_separados[0].strip()
        precio = lista_datos_separados[1].strip()
        cantidad = lista_datos_separados[2].strip()
        
        #Creamos el diccionario con las claves producto, precio, cantidad, y los valores con los datos del archivo productos.txt
        diccionario_productos = {"Producto": producto,"Precio": precio,"Cantidad": cantidad}

        #Creamos la lista de productos y le agremamos el diccionario
        lista_productos = []
        lista_productos.append(diccionario_productos)
        
        print(lista_productos)

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 5")

#Pedimos el producto que se va a buscar en el archivo
buscar_producto = str(input("Ingrese el nombre del producto que desea buscar: ")).capitalize()

#Bloque with para leer el archivo linea por linea
with open("productos.txt", "r") as archivo:
    for linea in archivo:

        #Condicional para verificar si el producto se encuentra en el archivo
        if buscar_producto in linea:
            print(linea)
            break

         #Si el producto no se encuentra en el archivo muestra un mensaje de error
        elif not buscar_producto in linea:
            print("El producto ingresado no se encuentra en la linea o en el archivo")

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 6")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto, Precio, Cantidad\n")
    archivo.write("Notebook, 2000, 5\n")
    archivo.write("Auriculares, 1200, 10\n")
    archivo.write("Mouse, 1000, 4\n")