print ("Martínez Estrada Ricardo / NO. de control: 1193 / 19-11-2024")
print (" ")

# Definimos la clase Calculadora
class Calculadora:
    # Método constructor que inicializa dos números
    def __init__(self, num1, num2):
        self._num1 = num1  # Primer número
        self._num2 = num2  # Segundo número

    # Método para realizar la suma
    def suma(self):
        resultado = self._num1 + self._num2  # Realizamos la suma
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    # Método para realizar la resta
    def resta(self):
        resultado = self._num1 - self._num2  # Realizamos la resta
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    # Método para realizar la división
    def division(self):
        # Verificamos si el divisor no es cero para evitar errores
        if self._num2 != 0:
            resultado = self._num1 / self._num2  # Realizamos la división
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")

    # Método para realizar la multiplicación
    def multiplicacion(self):
        resultado = self._num1 * self._num2  # Realizamos la multiplicación
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

# Crear instancias de Calculadora para realizar operaciones
operacion = Calculadora(10, 5)
operacion.suma()  # Resultado de la suma

operacion = Calculadora(20, 5)
operacion.resta()  # Resultado de la resta

operacion = Calculadora(15, 3)
operacion.division()  # Resultado de la división

operacion = Calculadora(8, 4)
operacion.multiplicacion()  # Resultado de la multiplicación