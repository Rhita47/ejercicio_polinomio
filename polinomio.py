from node import Node

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, power):
        # Añadir un término al polinomio, manteniendo el orden descendente por grado
        new_node = Node(coefficient, power)
        if self.head is None or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.power > power:
                current = current.next
            if current.next and current.next.power == power:
                current.next.coefficient += coefficient
                if current.next.coefficient == 0:
                    current.next = current.next.next
            else:
                new_node.next = current.next
                current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.power}", end=" + " if current.next else "")
            current = current.next
        print()

    @staticmethod
    def add(p1, p2):
        result = Polynomial()
        current1 = p1.head
        current2 = p2.head
        while current1 or current2:
            if current1 is None:
                result.add_term(current2.coefficient, current2.power)
                current2 = current2.next
            elif current2 is None:
                result.add_term(current1.coefficient, current1.power)
                current1 = current1.next
            elif current1.power > current2.power:
                result.add_term(current1.coefficient, current1.power)
                current1 = current1.next
            elif current1.power < current2.power:
                result.add_term(current2.coefficient, current2.power)
                current2 = current2.next
            else:
                sum_coeff = current1.coefficient + current2.coefficient
                if sum_coeff != 0:
                    result.add_term(sum_coeff, current1.power)
                current1 = current1.next
                current2 = current2.next
        return result

    @staticmethod
    def subtract(p1, p2):
        result = Polynomial()
        # Convertir los coeficientes del segundo polinomio en negativos para reutilizar el método add
        p2_neg = Polynomial()
        current = p2.head
        while current:
            p2_neg.add_term(-current.coefficient, current.power)
            current = current.next
        return Polynomial.add(p1, p2_neg)

    @staticmethod
    def multiply(p1, p2):
        result = Polynomial()
        current1 = p1.head
        while current1:
            current2 = p2.head
            while current2:
                result.add_term(current1.coefficient * current2.coefficient, current1.power + current2.power)
                current2 = current2.next
            current1 = current1.next
        return result

    @staticmethod
    def divide(p1, p2):
        # La división de polinomios es más compleja y se recomienda usar una biblioteca matemática
        # Aquí se proporciona un esqueleto básico
        print("La división de polinomios no está implementada en este ejemplo.")
        return None
