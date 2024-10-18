# Traducciones de español a inglés
print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_1199_3w_pr4")
print(" ")
traducciones_input = "perro:dog,casa:house,medicina:medicine"

# Crear un diccionario de traducción
traducciones = {}
for par in traducciones_input.split(','):
    espanol, ingles = par.split(':')
    traducciones[espanol.strip()] = ingles.strip()

# Solicitar una frase en español para traducir
frase = input("Introduce una frase en español para traducir:\n")

# Traducir la frase palabra por palabra
frase_traducida = []
for palabra in frase.split():
    traduccion = traducciones.get(palabra, palabra)  # Mantiene la palabra original si no se encuentra
    frase_traducida.append(traduccion)

# Mostrar la frase traducida
print("Frase traducida:", ' '.join(frase_traducida))
