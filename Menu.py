import random
import cProfile

# crear numeros aleatorios
def crear_numeros(cantidad, minimo, maximo, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(cantidad):
            numero = random.randint(minimo, maximo)
            archivo.write(str(numero) + '\n')

# leer un numero
def leer_numeros_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]
    return numeros

# algoritmos investigados anteriormente
def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# menu
def mostrar_menu():
    print("¿Qué algoritmo desea utilizar?")
    print("1. Gnome Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Radix Sort")
    print("5. Selection Sort")
    print("6. Shell Sort")
    print("7. Heap Sort")

# ascendente o descendente
def ordenar_numeros(algoritmo, numeros, ascendente=True):
    if algoritmo == 1:
        gnome_sort(numeros)
    elif algoritmo == 2:
        merge_sort(numeros)
    elif algoritmo == 3:
        quick_sort(numeros)
    elif algoritmo == 4:
        radix_sort(numeros)
    elif algoritmo == 5:
        selection_sort(numeros)
    elif algoritmo == 6:
        shell_sort(numeros)
    elif algoritmo == 7:
        heap_sort(numeros)
    
    if not ascendente:
        numeros.reverse()
    
    return numeros

def main():
    cantidad_numeros = 3000
    minimo = 0
    maximo = 10000
    nombre_archivo = 'numeros.txt'

    crear_numeros(cantidad_numeros, minimo, maximo, nombre_archivo)
    numeros = leer_numeros_desde_archivo(nombre_archivo)
    #mostrar menu
    mostrar_menu()
    algoritmo = int(input("Seleccione el algoritmo (1-7): "))

    # Solicitar al usuario informacion
    opcion = input("¿Desea ordenarlo de manera ascendente o descendente? (ascendente/descendente): ")
    ascendente = opcion.lower() == "ascendente"

    # Llamar a la función 
    sorted_numbers = ordenar_numeros(algoritmo, numeros, ascendente)

    # para verificar que si se ordenaran se imprimen los primeros 10
    print("Números ordenados:", sorted_numbers[:10])

    cProfile.runctx("ordenar_numeros(algoritmo, numeros, ascendente)", globals(), locals())

if __name__ == "__main__":
    main()
