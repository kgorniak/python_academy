print("test")

# zmienna zespolona
z = 1 + 2j

# zmienna całkowita - integer
a_int = 1

# zmienna przecinkowa
b_float = 2.5
c_float = 2e5

# zmienna tekstowa
d_string = "t\"ext"
e_string = "t'ext"

# lista
# 1.mutable - (can be edited), 2.ordered, 3.can be repeated
f_list = [1, 2.5, 'abc', [3, 4, 5], 5, 100]
f_list.append("test")
f_list.remove(2.5)
del f_list[2]
print(f_list[-1])   # negative indexes
print(f_list[1:4])  # slicing

# tuple
# not mutable, ordered, can be repeated
h_tuple = (1, 2, 3)

# słownik
# mutable, not ordered, keys unique
g_dict = {"title": "Harry Potter", "author": "J.K. Rowling", "items": 2}
print(g_dict["title"])
g_dict["cover"] = "hard"
print(g_dict)

# sety
# zbiór unikalnych wartości
h_set = {0, 2, 1, 2}
print(h_set)

# zmienne binarne True/False - boolean
i_bool = True
j_bool = False

# inicjalizowanie zmiennej bez konkretnego typu
k_none = None

print(str(i_bool))

car = {"name": "audi",
       "year": 2008,
       "seats": 5,
       "engine": 2.0,
       "ABS": True,
       "equipment": ("engine", "wheels", "seats"),
       "additional equipment": ["brakes", "mirrors", ]}
print(car)

######################################

hobby = "sleeping"
print("I like " + hobby + " a lot")
print("I like {} a lot".format(hobby))    #interpolacja
print(f"I like {hobby} a lot\n")     #f-strings

print(f"My car is {car['name']}. Year of production: {car['year']}.")
print("My car is {}.".format(car['name']))
print("My car has " + str(car['seats']) + " places.")

