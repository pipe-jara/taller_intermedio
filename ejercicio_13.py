# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.


while True:
    print("\n---menu principal---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")
    opcion = input("Selecciona una opcion: ")

    

    if opcion == "1":
        num_1 = float(input("ingrese el primer numero: "))
        num_2 = float(input("ingrese el segundo numero: "))
        suma = num_1 + num_2
        print("La suma es: ", (suma))
    elif opcion == "2":
        num_1 = float(input("ingrese el primer numero: "))
        num_2 = float(input("ingrese el segundo numero: "))
        resta = num_1 - num_2
        print("La suma es: ", (resta))
    elif opcion == "3":
        num_1 = float(input("ingrese el primer numero: "))
        num_2 = float(input("ingrese el segundo numero: "))
        mult = num_1 * num_2
        print("La suma es: ", (mult))
    elif opcion == "4":
        break
    else:
        print("Opcion Invalida")