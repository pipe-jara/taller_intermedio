# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.

password = "abcd1234"
intentos = 0
acceso = False

while intentos < 3:
    ingreso = input("ingrese la contraseña: ")
    if ingreso == password:
        acceso = True
        break
    intentos += 1

if acceso:
    print("¡Acceso concedido!")
else:
    print("Usuario bloqueado")
