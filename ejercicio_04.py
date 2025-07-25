# Múltiplos de 3
# Escribe un programa que imprima todos los múltiplos de 3 entre 1 y 100.


for i in range(1, 100 + 1):
    if i % 3 == 0:
        print(f"{i} Es multiplo de 3")
    else:
        print(i)

