# task description: https://adventofcode.com/2022/day/5

with open("day5_input.txt", "r") as file:
    read_file = file.readlines()
    all_lines_list = []
    for line in read_file:
        all_lines_list.append(line.rstrip())

# parsowanie początkowego stanu stosów do list (poziomo)
lines_all = []
for line in all_lines_list[:8]:
    # print(line)
    stack = []
    stack.append(line[:3].strip())
    stack.append(line[4:7].strip())
    stack.append(line[8:11].strip())
    stack.append(line[12:15].strip())
    stack.append(line[16:19].strip())
    stack.append(line[20:23].strip())
    stack.append(line[24:27].strip())
    stack.append(line[28:31].strip())
    stack.append(line[32:35].strip())
    lines_all.append(stack)
# print(lines_all)

# stworzenie stosów w liście
stacks_list = []
for counter in range(len(lines_all) + 1):
    stack = []
    for item in lines_all:
        stack.append(item[counter])
    stack.reverse()
    stacks_list.append(stack)
# print(stacks_list)

# usunięcie pustych ('') miejsc na stosach
for item in stacks_list:
    item[:] = [letter for letter in item if letter != '']
print(stacks_list)

# wrzucenie instrukcji do listy
instructions_list = []
for line in all_lines_list[10:]:
    instruction = line.split()
    instructions_list.append(instruction)
# print(instructions_list)

# part 1
# użycie instrukcji (przekładanie skrzyń na stosach - pojedynczo)
for instruction in instructions_list:
    how_many_to_move = int(instruction[1])
    from_stack = int(instruction[3]) - 1
    to_stack = int(instruction[5]) - 1
    for i in range(how_many_to_move):
        moving_item = stacks_list[from_stack][-1]
        del stacks_list[from_stack][-1]
        stacks_list[to_stack].append(moving_item)

# wyciągnięcie wyniku końcowego
text_answer = ""
for stack in stacks_list:
    text_answer += stack[-1].rstrip("]").lstrip("[")
print(f"Answer part 1 : {text_answer}\n")

# part 2
