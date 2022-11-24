for i in range(1, 10, 2):
    print(i)

fruits = ["apple", "banana", "grape", "error", "ananas"]
name = "krzy5ztof"

for fruit in fruits:
    if fruit == "error":
        break
    print(fruit)

for i in name:
    if i in "1234567890":
        print(f"{i} is not a letter!")
        break
    print(i)

# a, b = 0, 10
#
# while a < b:
#     print(f"a = {a}, b = {b}")
#     a += 1
#
# for i in range(10, 99):
#     if i % 2 == 0:
#         print(i)
#
# a = 10
# while a < 100:
#     if a % 2 == 0:
#         print(a)
#         a += 2
