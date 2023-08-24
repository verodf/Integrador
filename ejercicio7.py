class Cuenta:
    def __init__(self):
        self.titular = input("Ingrese el nombre del titular: ")
        self.cantidad = float(input("Ingrese la cantidad inicial: "))
    
    def get_titular(self):
        return self.titular
    
    def set_titular(self, titular):
        self.titular = titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print("La cantidad ingresada es inválida.")

cuenta = Cuenta()
cuenta.mostrar()

cantidad_ingresar = float(input("Ingrese la cantidad a ingresar: "))
cuenta.ingresar(cantidad_ingresar)
cuenta.mostrar()

cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
cuenta.retirar(cantidad_retirar)
cuenta.mostrar()
