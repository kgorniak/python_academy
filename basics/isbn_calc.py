isbn = "030640615"
suma = 0
n = 1
for number in isbn:
    suma += int(number) * n
    n += 1
control_num = suma % 11
print(isbn + f"-{control_num}")

############### second solution

total_sum = 0
for i in range(len(isbn)):
    number = int(isbn[i])
    total_sum += number * (i + 1)
checksum = total_sum % 11
print(f"Checksum number = {checksum}")
