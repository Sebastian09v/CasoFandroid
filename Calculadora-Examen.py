class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2 if self.num2 != 0 else "No se puede dividir entre cero"

num1 = int(input("Ingresa el primer número porfavor: "))
num2 = int(input("Ingresa el segundo número porfavor: "))

calculadora = Calculadora(num1, num2)

print("Suma:", calculadora.suma())
print("Resta:", calculadora.resta())
print("Multiplicación:", calculadora.multiplicacion())
print("División:", calculadora.division())
