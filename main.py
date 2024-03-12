from polinomio import Polynomial

def create_polynomial():
    p = Polynomial()
    num_terms = int(input("¿Cuántos términos tiene el polinomio? "))
    for _ in range(num_terms):
        coefficient = float(input("Coeficiente: "))
        power = int(input("Potencia: "))
        p.add_term(coefficient, power)
    return p

def main():
    print("Defina el Polinomio 1")
    polynomial1 = create_polynomial()

    print("\nDefina el Polinomio 2")
    polynomial2 = create_polynomial()

    print("\nPolinomio 1:")
    polynomial1.display()

    print("Polinomio 2:")
    polynomial2.display()

    operation = input("\nSeleccione una operación (suma, resta, multiplicación, división): ").lower()

    if operation == "suma":
        result = Polynomial.add(polynomial1, polynomial2)
    elif operation == "resta":
        result = Polynomial.subtract(polynomial1, polynomial2)
    elif operation == "multiplicación":
        result = Polynomial.multiply(polynomial1, polynomial2)
    elif operation == "división":
        result = Polynomial.divide(polynomial1, polynomial2)
    else:
        print("Operación no reconocida.")
        return

    print("\nResultado:")
    result.display()

if __name__ == "__main__":
    main()
