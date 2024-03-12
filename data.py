from node import Node

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, power):
        new_node = Node(coefficient, power)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.power}", end=" + " if current.next else "")
            current = current.next
        print()  # Newline for better readability

    @staticmethod
    def add(p1, p2):
        # Placeholder for addition method
        pass

    @staticmethod
    def subtract(p1, p2):
        # Placeholder for subtraction method
        pass

    @staticmethod
    def multiply(p1, p2):
        # Placeholder for multiplication method
        pass

    @staticmethod
    def divide(p1, p2):
        # Placeholder for division method, might require implementation of polynomial long division
        pass
