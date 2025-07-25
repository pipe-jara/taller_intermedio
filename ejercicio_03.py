# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.


vocales = ("a, e, i, o, u")
palabra = input("Ingrese la palabra que desees: ")
conteo = 0

for letra in palabra:
    if letra.lower() in vocales:
        conteo += 1

print(f"la palabra '{palabra}' tiene {conteo} vocales")