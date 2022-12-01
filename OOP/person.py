from datetime import date

class Person:

    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
        print(self.name, self.surname)

    def return_age(self):
        current_year = date.today().year
        return current_year - self.year_of_birth

    def change_surname(self, new_surname):
        self.surname = new_surname


person = Person("ala", "kot", 1991)
person.print_full_name()
print(person.return_age())
# person.change_surname("pies")
person.change_surname("pies")
person.print_full_name()
