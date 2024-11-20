print ("Martínez Estrada Ricardo / NO. de control: 1193 / 19-11-2024")
print (" ")

class Estudiante:
    # Método constructor que inicializa el nombre y la nota del estudiante
    def __init__(self, nombre, nota):
        self.nombre = nombre  # Atributo para almacenar el nombre del estudiante
        self.nota = nota      # Atributo para almacenar la nota del estudiante

    # Método para imprimir los datos del estudiante
    def imprimir(self):
        # Usamos una cadena formateada para mostrar nombre y nota
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    # Método para determinar si el estudiante aprobó o reprobó
    def resultados(self):
        # Si la nota es mayor o igual a 7, se considera aprobado
        if self.nota >= 7:
            print("¡Has APROBADO!")  # Mensaje para estudiantes aprobados
        else:
            print("¡Has REPROBADO!")  # Mensaje para estudiantes reprobados

# Crear una instancia de la clase Estudiante con nombre "Pedro" y nota 5
estudiante1 = Estudiante("Pedro", 5)
estudiante1.imprimir()  # Imprime los datos de "Pedro"
estudiante1.resultados()  # Muestra si "Pedro" aprobó o reprobó

# Crear otra instancia de la clase Estudiante con nombre "Elizabeth" y nota 7
estudiante2 = Estudiante("Elizabeth", 7)
estudiante2.imprimir()  # Imprime los datos de "Elizabeth"
estudiante2.resultados()  # Muestra si "Elizabeth" aprobó o reprobó