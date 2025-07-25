# Iteración sobre tuplas
# Define la tupla (10, 20, 30, 40, 50) y recórrela con un for
# para imprimir cada elemento y su índice (usa enumerate).

numeros = (10, 20, 30, 40, 50)

for i, n in enumerate(numeros):
    print(f"Indice {i}: {n}")