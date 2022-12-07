from datetime import date


class Person:

    def __init__(self, name, surname, year_of_birth):
        # self._name = name   # protected
        # self.__surname = surname    # private
        self.name = name
        self._surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
        print(self.name, self.surname)

    def return_age(self):
        current_year = date.today().year
        return current_year - self.year_of_birth

    def change_surname(self, new_surname):
        self.surname = new_surname

    @property   # getter
    def surname(self):
        return self._surname

    @surname.setter     # setter
    def surname(self, new_surname):
        self._surname = new_surname

if __name__ == "__main__":
    ala = Person("alaa", "kot", 1991)
    # print(ala._name)    # access to protected
    # print(ala._Person__surname)     # access to private *
    print(ala.surname)      # getter
    ala.surname = "NOWE NAZWISKO"   # setter
    print(ala.print_full_name())


