from oop.person import Person
from math import ceil


class Travel(Person):

    def __init__(self, name, surname, year_of_birth, distance):
        super().__init__(name, surname, year_of_birth)
        self.distance = distance
        self.passport_dict = {}

    def calculate_cost(self):
        if self.return_age() < 5:
            cost = 0
        elif 5 <= self.return_age() <= 26:
            cost = (ceil(self.distance / 100) * 10) * 0.49
        else:
            cost = ceil(self.distance / 100) * 10
        return cost

    @property
    def passport(self):
        return self.passport_dict

    @passport.setter
    def passport(self, countries):
        for country in countries:
            if country not in self.passport_dict.keys():
                self.passport_dict[country] = 1
            else:
                self.passport_dict[country] += 1


if __name__ == "__main__":
    traveler = Travel("andrzej", "testowy", year_of_birth=2000, distance=9999)
    print(f"Cost of travel = {traveler.calculate_cost()}")

    print(traveler.passport)
    traveler.passport = ["Poland", "Germany", "Spain"]
    print(traveler.passport)
    traveler.passport = ["Poland", "Germany", "Spain", "England", "Spain"]
    print(traveler.passport)
