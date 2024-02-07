import random

def crearnumeros(cantidad, minimo, maximo, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(cantidad):
            numero = random.randint(minimo, maximo)
            archivo.write(str(numero) + '\n')

def leer_numeros_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]
    return numeros

cantidad_numeros = 3000
minimo = 10
maximo = 10000
nombre_archivo = 'numeros.txt'

crearnumeros(cantidad_numeros, minimo, maximo, nombre_archivo)

numeros = leer_numeros_desde_archivo(nombre_archivo)
print("Números generados en el archivo numeros.txt")  
