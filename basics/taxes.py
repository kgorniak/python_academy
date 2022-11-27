annual_salary = int(input(f"Provide your annual salary: "))

if 0 < annual_salary <= 30000:
    print("Tax = 0")
elif 30001 <= annual_salary <= 120000:
    tax = (0.12 * annual_salary) - 3600
    print(f"Tax = {tax}")
elif annual_salary >= 120001:
    tax = 10800 + ((annual_salary - 120000) * 0.32)
    print(f"Tax = {tax}")
