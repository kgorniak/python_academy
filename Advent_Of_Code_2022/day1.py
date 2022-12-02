# task description: https://adventofcode.com/2022/day/1

with open("day1_data.txt", "r") as file:
    read_file = file.readlines()

single_elf_calories = []
elfs_calories = []
for calories in read_file:
    if calories != "\n":
        calories = int(calories.strip())
        single_elf_calories.append(calories)
    elif calories == "\n":
        elfs_calories.append(single_elf_calories)
        single_elf_calories = []

print(f"{elfs_calories}\n")

sum_calories = []
for i in elfs_calories:
    sum_calories.append(sum(i))

print(f"{sum_calories}\n")

sorted_calories = sorted(sum_calories, reverse=True)
print(sorted_calories)
top_3_sum_calories = 0
for i in range(3):
    top_3_sum_calories += sorted_calories[i]
print(f"Top 3 sum calories = {top_3_sum_calories}")

highest_calories = max(sum_calories)
print(f"Highest calories = {highest_calories}")
