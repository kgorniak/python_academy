from datetime import date


class Person:
    def __init__(self, name: str, surname: str, year_of_birth: int):
        self.name = name
        self.surname = surname
        self.__year_of_birth = year_of_birth

    def print_full_name(self):
        print(self.name, self.surname)

    def return_age(self) -> int:
        current_year = date.today().year
        return current_year - self.__year_of_birth

    def change_surname(self, new_surname):
        self.surname = new_surname


class Employee(Person):
    def __init__(
        self, name: str, surname: str, year_of_birth: int, type_of_employment: str
    ):
        super().__init__(name, surname, year_of_birth)
        self.type_of_employment = type_of_employment

    def change_employment_type(self, new_type: str):
        self.type_of_employment = new_type


class Student(Person):
    def __init__(
        self,
        name: str,
        surname: str,
        year_of_birth: int,
        student_id: str,
        initial_grades=None,
    ):
        super().__init__(name, surname, year_of_birth)
        if initial_grades is None:
            initial_grades = []
        self.initial_grades = initial_grades
        self._student_id = student_id

    def add_grade(self, grade: int):
        if type(grade) is not int:
            return False
        self.initial_grades.append(grade)

    def calculate_final_grade(self) -> float:
        final_grade = round(sum(self.initial_grades) / len(self.initial_grades))
        return final_grade

    def clear_all_grades(self):
        self.initial_grades = []

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new_id):
        self._student_id = new_id


if __name__ == "__main__":
    student = Student("Jan", "Kowalski", 1999, "#123", [2, 3, 4])
    student.add_grade(5)
    student.add_grade(4)
    student.add_grade(3)
    print(f"Grades: {student.initial_grades}")
    print(f"Final grade = {student.calculate_final_grade()}")
    student.clear_all_grades()
    print(f"Grades after clear: {student.initial_grades}")
    print(f"(protected) ID: {student.student_id}")
    student.student_id = "#987"
    print(f"ID after change: {student.student_id}")

    # andrzej_programmer = Employee("Andrzej", "Programmer", 1999, "B2B")
    # andrzej_programmer.print_full_name()
    #
    # person = Person("ala", "kot", 1991)
    # person.print_full_name()
    # print(person.return_age())
    # # person.change_surname("pies")
    # person.change_surname("pies")
    # person.print_full_name()
