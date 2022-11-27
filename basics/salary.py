salary = int(input("Provide your basic salary: "))

if salary <= 10000:
    hra = salary * 0.2
    da = salary * 0.8
    print(f"House Rent Allowance = {hra}\nDearness Allowance = {da}")
elif 10001 <= salary <= 20000:
    hra = salary * 0.25
    da = salary * 0.9
    print(f"House Rent Allowance = {hra}\nDearness Allowance = {da}")
elif salary > 20000:
    hra = salary * 0.30
    da = salary * 0.95
    print(f"House Rent Allowance = {hra}\nDearness Allowance = {da}")
