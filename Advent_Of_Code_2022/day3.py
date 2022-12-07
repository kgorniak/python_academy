# task description: https://adventofcode.com/2022/day/3
import string

# first part
counter = 1
dict_lower_case = {}
for i in string.ascii_lowercase:
    dict_lower_case[i] = counter
    counter += 1
# print(dict_lower_case)

dict_upper_case = {}
for i in string.ascii_uppercase:
    dict_upper_case[i] = counter
    counter += 1

dict_upper_case.update(dict_lower_case)
# print(dict_upper_case)

with open("day3_input.txt", "r") as file:
    read_file = file.readlines()
    rucksacks_list = []
    for i in read_file:
        rucksacks_list.append(i.strip())
# print(rucksack_list)

repeated_letters_list = []
for rucksack in rucksacks_list:
    rucksack_half = int(len(rucksack) / 2)
    first_compartment = rucksack[:rucksack_half]
    second_compartment = rucksack[rucksack_half:]
    # print(f"First : {first_compartment}, Second : {second_compartment}")

    for letter in first_compartment:
        if letter in second_compartment:
            repeated_letters_list.append(letter)
            break

sum_of_priorities = 0
# print(repeated_letters_list)
for letter in repeated_letters_list:
    if letter in dict_upper_case.keys():
        sum_of_priorities += dict_upper_case[letter]
print(f"First part answer : {sum_of_priorities}")

# part 2
group = []
group_list = []
for i in rucksacks_list:
    if len(group) == 3:
        group_list.append(group)
        group = []
        group.append(i)
    else:
        group.append(i)
group_list.append(group)
# print(group_list)

