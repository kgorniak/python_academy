a = 10
if a > 0 and a < 100:
    print("Value is positive")
elif a == 0:
    print("Value is 0")
else:
    print("Value is negative")

distances = {"Nicosia": 1980,
             "Reykjavik": 2900,
             "Chartum": "not exist",
             "Gdansk": 485}

destination = "Nicosia"
if destination == "Nicosia":
    cost = 2 * distances[destination]
    if distances[destination] > 2000:
        cost += 100
    print(f"Travel cost to {destination} is: {cost}")
elif destination == "Reykjavik":
    cost = 2 * distances[destination]
    if distances[destination] > 2000:
        cost += 100
    print(f"The travel cost to {destination} is: {cost}")
elif destination == "Gdansk":
    cost = 2 * distances[destination]
    if distances[destination] > 2000:
        cost += 100
    print(f"Travel cost to {destination} is: {cost}")
else:
    print(f"Travel cost to {destination} is not available")

