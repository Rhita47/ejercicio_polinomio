
class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo_nodo = Nodo(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def evaluar(self, x):
        resultado = 0
        actual = self.cabeza
        while actual is not None:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return resultado

    def sumar(self, otro_polinomio):
        resultado = Polinomio()
        actual1 = self.cabeza
        actual2 = otro_polinomio.cabeza
        while actual1 is not None or actual2 is not None:
            if actual1 is None:
                resultado.agregar_termino(actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente
            elif actual2 is None:
                resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            elif actual1.exponente > actual2.exponente:
                resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            elif actual1.exponente < actual2.exponente:
                resultado.agregar_termino(actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente
            else:
                coeficiente_suma = actual1.coeficiente + actual2.coeficiente
                if coeficiente_suma != 0:
                    resultado.agregar_termino(coeficiente_suma, actual1.exponente)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
        return resultado

    def restar(self, otro_polinomio):
        resultado = Polinomio()
        actual1 = self.cabeza
        actual2 = otro_polinomio.cabeza
        while actual1 is not None or actual2 is not None:
            if actual1 is None:
                resultado.agregar_termino(-actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente
            elif actual2 is None:
                resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            elif actual1.exponente > actual2.exponente:
                resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            elif actual1.exponente < actual2.exponente:
                resultado.agregar_termino(-actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente
            else:
                coeficiente_resta = actual1.coeficiente - actual2.coeficiente
                if coeficiente_resta != 0:
                    resultado.agregar_termino(coeficiente_resta, actual1.exponente)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
        return resultado

    def multiplicar(self, otro_polinomio):
        resultado = Polinomio()
        actual1 = self.cabeza
        while actual1 is not None:
            actual2 = otro_polinomio.cabeza
            while actual2 is not None:
                coeficiente_producto = actual1.coeficiente * actual2.coeficiente
                exponente_suma = actual1.exponente + actual2.exponente
                resultado.agregar_termino(coeficiente_producto, exponente_suma)
                actual2 = actual2.siguiente
            actual1 = actual1.siguiente
        return resultado

# Pedir término y valor por pantalla
termino = input("Ingrese el término: ")
valor = float(input("Ingrese el valor: "))

# Crear instancia de Polinomio
polinomio1 = Polinomio()
polinomio1.agregar_termino(1, 2)
polinomio1.agregar_termino(2, 1)
polinomio1.agregar_termino(3, 0)

polinomio2 = Polinomio()
polinomio2.agregar_termino(4, 3)
polinomio2.agregar_termino(5, 2)
polinomio2.agregar_termino(6, 1)

# Evaluar el polinomio en el valor dado
resultado1 = polinomio1.evaluar(valor)
resultado2 = polinomio2.evaluar(valor)
print(f"El resultado de evaluar el polinomio1 en {valor} es: {resultado1}")
print(f"El resultado de evaluar el polinomio2 en {valor} es: {resultado2}")

# Sumar los polinomios
suma = polinomio1.sumar(polinomio2)
print(f"La suma de los polinomios es: {suma}")

# Restar los polinomios
resta = polinomio1.restar(polinomio2)
print(f"La resta de los polinomios es: {resta}")

# Multiplicar los polinomios
producto = polinomio1.multiplicar(polinomio2)
print(f"El producto de los polinomios es: {producto}")  
