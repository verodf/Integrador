def calcular_LCM():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))


    
    # Calculamos el máximo común divisor (MCD) 
    def calcular_MCD(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Obtenemos el MCD
    mcd = calcular_MCD(a, b)

    # Calculamos LCM = (a * b) / MCD
    lcm = (a * b) // mcd

    return lcm

# Llamada a la función
resultado_lcm = calcular_LCM()
print("El mínimo común múltiplo es:", resultado_lcm)
