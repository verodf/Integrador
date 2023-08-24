class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""

    def set_nombre(self, nombre):
        if not nombre.isnumeric() and not any(char.isdigit() for char in nombre):
            self.nombre = nombre
        else:
            print("El nombre no puede ser numérico ni contener números.")

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if isinstance(dni, int) and len(str(dni)) == 8:
            self.dni = dni
        else:
            print("El DNI debe ser un número entero de 8 dígitos.")

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Crear un objeto de la clase Persona
persona = Persona()

# Ingresar los datos por teclado
nombre = input("Ingrese el nombre: ")
persona.set_nombre(nombre)

while True:
    try:
        edad = int(input("Ingrese la edad: "))
        persona.set_edad(edad)
        break
    except ValueError:
        print("La edad debe ser un número.")

while True:
    try:
        dni = int(input("Ingrese el DNI (8 dígitos): "))
        persona.set_dni(dni)
        break
    except ValueError:
        print("El DNI debe ser un número entero.")

# Obtener los atributos utilizando los métodos get
nombre = persona.get_nombre()
edad = persona.get_edad()
dni = persona.get_dni()

# Mostrar los datos de la persona
persona.mostrar()

# Verificar si la persona es mayor de edad
es_mayor = persona.es_mayor_de_edad()
print("¿Es mayor de edad?", es_mayor)


