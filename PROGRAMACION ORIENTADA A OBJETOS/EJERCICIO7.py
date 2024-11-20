print ("Martínez Estrada Ricardo / NO. de control: 1193 / 19-11-2024")
print (" ")

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.nombre}")

persona = Estudiante("Harvard")
persona.carrera("Ingeniería mecatrónica")
persona.datos("Mike", 19)