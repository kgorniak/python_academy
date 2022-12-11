import math


def calculate_fuel(mass):
    if type(mass) is int:
        if 9 <= mass > 0:
            needed_fuel = int(mass / 3) - 2
    # needed_fuel = mass // 3 - 2
    # needed_fuel = math.floor(mass / 3) - 2
            return needed_fuel
        elif mass <= 0:
            return False
        else:
            return 1
    elif type(mass) is not int:
        return False

# print(calculate_fuel(14))
