def get_int():
    try:
        num = int(input("Ingrese un número entero (recursiva): "))
        return num
    except ValueError:
        print("Valor incorrecto de manera recursiva. Intente nuevamente.")
        return get_int()

def get_int_iterative():
    while True:
        try:
            num = int(input("Ingrese un número entero (iterativa): "))
            return num
        except ValueError:
            print("Valor incorrecto de manera iterativa. Intente nuevamente.")

# Llamada a ambas funciones
num_recursivo = get_int()
num_iterativo = get_int_iterative()

# Imprimir los números ingresados
print("Número ingresado de manera recursiva:", num_recursivo)
print("Número ingresado de manera iterativa:", num_iterativo)
