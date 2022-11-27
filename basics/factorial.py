number = int(input("Please give an integer to count factorial: "))

factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(factorial)
