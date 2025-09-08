from source.calculator import BasicCalculator


def test_addition_10_5():
    object = BasicCalculator()
    object.provide_number(10)
    object.provide_operand('+')
    object.provide_number(5)
    # print(object.show_result())
    assert object.show_result()[0] == 15


def test_subtraction():
    object = BasicCalculator()
    object.provide_number(13)
    object.provide_operand('-')
    object.provide_number(21)
    assert object.show_result()[0] == -8


def test_multiplication():
    object = BasicCalculator()
    object.provide_number(3)
    object.provide_operand('*')
    object.provide_number(22)
    assert object.show_result()[0] == 66


def test_division():
    object = BasicCalculator()
    object.provide_number(77)
    object.provide_operand('/')
    object.provide_number(11)
    assert object.show_result()[0] == 7


def test_addition_2_m4():
    object = BasicCalculator()
    object.provide_number(2)
    object.provide_operand('+')
    object.provide_number(-4)
    assert object.show_result()[0] == -2


def test_addition_m10_12():
    object = BasicCalculator()
    object.provide_number(-10)
    object.provide_operand('+')
    object.provide_number(12)
    assert object.show_result()[0] == 2


def test_subtraction_m3_m7():
    object = BasicCalculator()
    object.provide_number(-3)
    object.provide_operand('-')
    object.provide_number(-7)
    assert object.show_result()[0] == 4
