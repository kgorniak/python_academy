pesel = input("Please provide your PESEL: ")
MULTIPLIER = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
multi_sum = 0

for i in range(len(pesel) - 1):
    multi_sum += int(pesel[i]) * MULTIPLIER[i]

m_value = multi_sum % 10
if m_value == 0 and int(pesel[-1]) == 0:
    print("Proper PESEL")
else:
    control_num = 10 - m_value
    if control_num == int(pesel[-1]):
        print(f"Proper PESEL")
    else:
        print(f"{pesel} wrong PESEL number.")
