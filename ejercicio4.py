def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    max_frecuencia = max(diccionario.values())
    palabra = [k for k, v in diccionario.items() if v == max_frecuencia][0]
    return (palabra, max_frecuencia)

# Pedir al usuario que ingrese una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Llamar a la función contar_palabras() y mostrar el resultado
resultado_diccionario = contar_palabras(cadena)
print("Diccionario de palabras y frecuencias:")
print(resultado_diccionario)

# Llamar a la función palabra_mas_repetida() y mostrar el resultado
resultado_tupla = palabra_mas_repetida(resultado_diccionario)
print("Palabra más repetida y su frecuencia:")
print(resultado_tupla)
