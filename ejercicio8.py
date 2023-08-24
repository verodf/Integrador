class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
    
    def retirar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print("Se ha retirado", cantidad, "de la cuenta.")
        else:
            print("No hay suficiente saldo en la cuenta.")

class CuentaJoven(Cuenta):
    def __init__(self, titular="", cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def es_titular_valido(self):
        while True:
            try:
                edad = int(input("Ingrese la edad del titular: "))
                if edad >= 18 and edad < 25:
                    return True
                else:
                    print("El titular debe tener entre 18 y 24 años.")
            except ValueError:
                print("Ingrese una edad válida.")
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            cantidad_con_bonificacion = cantidad + (cantidad * self.bonificacion / 100)
            if cantidad_con_bonificacion <= self.cantidad:
                self.cantidad -= cantidad
                print("Se ha retirado", cantidad_con_bonificacion, "de la cuenta.")
            else:
                print("No hay suficiente saldo en la cuenta.")
        else:
            print("El titular no es válido para realizar la retirada de dinero.")
    
    def mostrar(self):
        print("Cuenta Joven")
        print("Titular:", self.titular)
        print("Saldo:", self.cantidad)
        print("Bonificación:", self.bonificacion, "%")


cuenta_joven = CuentaJoven("Veronica DF", 1000, 5)
cuenta_joven.mostrar()

cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
cuenta_joven.retirar(cantidad_retirar)
cuenta_joven.mostrar()
