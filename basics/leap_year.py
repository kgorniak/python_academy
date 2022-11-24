year = 2006

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is leap")
elif year % 400 == 0:
        print(f"{year} is leap")
else:
    print(f"{year} is not leap")