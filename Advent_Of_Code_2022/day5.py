# task description: https://adventofcode.com/2022/day/5

with open("day5_input.txt", "r") as file:
    read_file = file.readlines()
    all_lines_list = []
    for line in read_file:
        all_lines_list.append(line.rstrip())

# parsowanie początkowego stanu stosów do list

current_line = 1
for line in all_lines_list:
    while current_line < 9:
        print(line)
        current_line += 1
        break

# wrzucenie instrukcji do listy/słownika
