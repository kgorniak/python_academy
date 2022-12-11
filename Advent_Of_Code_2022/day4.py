# task description: https://adventofcode.com/2022/day/4

with open("day4_input.txt", "r") as file:
    read_file = file.readlines()
    rows_list = []
    for i in read_file:
        rows_list.append(i.strip())

contains_pairs = 0
# part 1
# print(rows_list[0])
for row in rows_list:
    sections = row.split(",")
    first_section = sections[0]
    second_section = sections[1]
    first_section_split = first_section.split("-")
    second_section_split = second_section.split("-")

    first_numbers = []
    second_numbers = []
    for i in range(int(first_section_split[0]), int(first_section_split[1]) + 1):
        first_numbers.append(i)
    for i in range(int(second_section_split[0]), int(second_section_split[1]) + 1):
        second_numbers.append(i)

    if (first_numbers[0] in second_numbers) and (first_numbers[-1] in second_numbers):
        contains_pairs += 1
    elif (second_numbers[0] in first_numbers) and (second_numbers[-1] in first_numbers):
        contains_pairs += 1

print(f"Answer part 1: {contains_pairs}")

# part 2
overlap_pairs = 0

for row in rows_list:
    sections = row.split(",")
    first_section = sections[0]
    second_section = sections[1]
    first_section_split = first_section.split("-")
    second_section_split = second_section.split("-")

    first_numbers = []
    second_numbers = []
    for i in range(int(first_section_split[0]), int(first_section_split[1]) + 1):
        first_numbers.append(i)
    for i in range(int(second_section_split[0]), int(second_section_split[1]) + 1):
        second_numbers.append(i)

    for number in first_numbers:
        if number in second_numbers:
            overlap_pairs += 1
            break

print(f"Second part answer : {overlap_pairs}")
