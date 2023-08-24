def calcular_MCD_y_comprobar_mayor():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    # Determinar el número mayor
    mayor = max(a, b)

    # Algoritmo para calcular el MCD
    while b != 0:
        a, b = b, a % b

    mcd = a

    return mcd, mayor

# Llamada a la función
resultado_mcd, resultado_mayor = calcular_MCD_y_comprobar_mayor()
print("El máximo común divisor es:", resultado_mcd)
print("El número mayor es:", resultado_mayor)

