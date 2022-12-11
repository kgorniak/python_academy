class Calculator:

    def add(self, a, b):
        result = a + b
        return result

    def substract(self, a, b):
        result = a - b
        return result

    def multiply(self, a, b):
        result = a * b
        return result

    def devide(self, a, b):
        result = a / b
        return result

    def inverted(self, a):
        result = 1 / a
        return result

    def factorial(self, a):
        factorial = 1
        for i in range(2, a + 1):
            factorial *= i
        return factorial


# calculator = Calculator()
# calculator.add(3, 5)
# calculator.inverted(4)
# calculator.factorial(3)
