print("Martínez Estrada Ricardo / NO. de control: 1193 / 19-11-2024")
print(" ")

# Definimos la clase Persona
class Persona:
    # Método constructor que inicializa el nombre y la edad de la persona
    def __init__(self, n, e):
        self.nombre = n  # Atributo para almacenar el nombre de la persona
        self.edad = e    # Atributo para almacenar la edad de la persona

    # Método para incrementar la edad de la persona en 1 (cumpleaños)
    def cumpleaños(self):
        self.edad += 1  # Incrementa la edad en 1

# Crear una instancia de la clase Persona solicitando datos al usuario
nombre = input("Ingrese nombre: ")  # Pedimos el nombre
edad = int(input("Ingrese edad: "))  # Pedimos la edad (convertida a entero)
p = Persona(nombre, edad)  # Creamos el objeto de la clase Persona

# Llamamos al método cumpleaños una sola vez para incrementar la edad
p.cumpleaños()

# Mostramos el resultado final
print(f"{p.nombre} cumple {p.edad} años")