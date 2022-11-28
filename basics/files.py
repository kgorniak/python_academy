# 1st way (not recommended)

# file = open("text.txt", "r")
# print(file.read())
# file.close()

# 2nd way to open file
suma = 0
with open("text.txt", "r") as file:
    read_text = file.readlines()
    for i in read_text:
        suma += int(i)
print(suma)
