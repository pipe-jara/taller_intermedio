# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese un 0. Al finalizar,
# muestra la suma de todos los valores ingresados (excluyendo el cero).

suma = 0 

dato = int(input("Ingrese el numero que desea sumar (oprima 0 para terminar): "))

while dato != 0:
    suma += dato 
    print(suma)
    dato = int(input("Ingrese el numero que desea sumar (oprima 0 para terminar): "))

print(f"La suma total fue {suma}")