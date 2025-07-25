# Búsqueda con while-else
# Dada la lista [4, 8, 15, 16, 23, 42], pide al usuario un número a buscar.

# Recorre la lista con un while y, si lo encuentras, muestra su índice y haz break.

# Si terminas el bucle sin encontrarlo, el bloque else debe imprimir “Número no encontrado”.


lista = [4, 8, 15, 16, 23, 42]


numero = int(input("Ingresa el número que deseas buscar: "))


i = 0

while i < len(lista):
    if lista[i] == numero:
        print(f"Número {numero} encontrado en el índice {i}")
        break
    i += 1
else:
    print("Número no encontrado")
