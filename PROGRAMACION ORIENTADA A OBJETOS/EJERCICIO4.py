print ("Martínez Estrada Ricardo / NO. de control: 1193 / 19-11-2024")
print (" ")

# Clase base Persona
class Persona:
    # Método constructor que inicializa el nombre y el apellido
    def __init__(self, nom, ape):
        self.nombre = nom  # Atributo para almacenar el nombre
        self.apellido = ape  # Atributo para almacenar el apellido

    # Método para imprimir el nombre completo
    def nombre_completo(self):
        # Concatenamos nombre y apellido con un espacio entre ellos
        print(self.nombre + " " + self.apellido)


# Clase derivada Estudiante que hereda de Persona
class Estudiante(Persona):
    # Método constructor que inicializa nombre, apellido y carrera
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)  # Llamamos al constructor de la clase base
        self.carrera = carr  # Atributo adicional para almacenar la carrera

    # Método para mostrar la carrera del estudiante
    def mostrar_carrera(self):
        print(self.carrera)


# Crear una instancia de Persona y mostrar su nombre completo
persona1 = Persona("Carlos", "Pérez")
print("Persona:")
persona1.nombre_completo()  # Muestra el nombre completo de la persona

# Crear una instancia de Estudiante y mostrar su nombre completo y carrera
estudiante1 = Estudiante("Ana", "Gómez", "Ingeniería en Sistemas")
print("\nEstudiante:")
estudiante1.nombre_completo()  # Muestra el nombre completo del estudiante
estudiante1.mostrar_carrera()  # Muestra la carrera del estudiante