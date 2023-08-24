def contar_palabras(cadena):
  
    palabras = cadena.split()

    # Crear un diccionario para almacenar las palabras y su frecuencia
    frecuencia = {}

   
    for palabra in palabras:
        
        if palabra in frecuencia:
            frecuencia[palabra] += 1
       
        else:
            frecuencia[palabra] = 1

    return frecuencia

# Pedir al usuario que ingrese una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Llamar a la función contar_palabras() y mostrar el resultado
resultado = contar_palabras(cadena)
print("Resultado:")
print(resultado)
