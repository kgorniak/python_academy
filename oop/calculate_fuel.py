import math


def calculate_fuel(mass):
    needed_fuel = int(mass / 3) - 2
    # needed_fuel = mass // 3 - 2
    # needed_fuel = math.floor(mass / 3) - 2
    return needed_fuel


# print(calculate_fuel(14))
