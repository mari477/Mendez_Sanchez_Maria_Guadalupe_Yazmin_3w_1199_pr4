# Imprime espacios y la identificación del programa
print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_1199_3w_pr4")
print(" ")
# Inicializa un diccionario para almacenar la información
informacion = {}
# Bandera para controlar el ciclo
bandera = 1
# Inicia un bucle que se ejecuta mientras la bandera sea 1
while bandera == 1:
    # Solicita al usuario que ingrese el tipo de información a agregar
    dato = input("¿Qué información vas a agregar? (nombre, edad, sexo, teléfono, correo electrónico, etc)\n").lower()
    print(" ")
    # Solicita al usuario que ingrese el valor correspondiente a la información
    valor = input("Escribe el dato:\n")
    print(" ")
    # Agrega el dato y su valor al diccionario
    informacion[dato] = valor
    # Imprime el diccionario actualizado
    print(informacion)
    # Pregunta al usuario si desea continuar o no
    print("¿Quieres seguir ejecutando el programa?\nPresione 1 para continuar, de lo contrario presione 2")
    print(" ")
    # Lee la opción del usuario para continuar o salir
    bandera = int(input())
    print(" ")
# Mensaje final cuando el programa termina
print("FIN")

