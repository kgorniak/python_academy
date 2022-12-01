class Calculator:

    def add(self, a, b):
        result = a + b
        print(result)

    def substract(self, a, b):
        result = a - b
        print(result)

    def multiply(self, a, b):
        result = a * b
        print(result)

    def devide(self, a, b):
        result = a / b
        print(result)

    def inverted(self, a):
        result = 1 / a
        print(result)

    def factorial(self, a):
        factorial = 1
        for i in range(2, a + 1):
            factorial *= i
        print(factorial)


calculator = Calculator()
calculator.add(3, 5)
calculator.inverted(4)
calculator.factorial(3)
