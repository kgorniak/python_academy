import copy

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
stacks_list_master = []
for counter in range(len(lines_all) + 1):
    stack = []
    for item in lines_all:
        stack.append(item[counter])
    stack.reverse()
    stacks_list_master.append(stack)
# print(stacks_list)

# usunięcie pustych ('') miejsc na stosach
for item in stacks_list_master:
    item[:] = [letter for letter in item if letter != '']
# print(stacks_list_master)

# wrzucenie instrukcji do listy
instructions_list = []
for line in all_lines_list[10:]:
    instruction = line.split()
    instructions_list.append(instruction)
# print(instructions_list)

# part 1
# użycie instrukcji (przekładanie skrzyń na stosach - pojedynczo)
stacks_list1 = copy.deepcopy(stacks_list_master)
for instruction in instructions_list:
    how_many_to_move = int(instruction[1])
    from_stack = int(instruction[3]) - 1
    to_stack = int(instruction[5]) - 1
    for i in range(how_many_to_move):
        moving_item = stacks_list1[from_stack][-1]
        del stacks_list1[from_stack][-1]
        stacks_list1[to_stack].append(moving_item)

# wyciągnięcie wyniku końcowego
text_answer1 = ""
for stack in stacks_list1:
    text_answer1 += stack[-1].rstrip("]").lstrip("[")
print(f"Answer part 1 : {text_answer1}\n")

# part 2
# użycie instrukcji (przekładanie skrzyń na stosach - po kilka na raz)
stacks_list2 = copy.deepcopy(stacks_list_master)
for instruction in instructions_list:
    how_many_to_move = int(instruction[1])
    from_stack = int(instruction[3]) - 1
    to_stack = int(instruction[5]) - 1
    moving_items = stacks_list2[from_stack][-how_many_to_move:]
    del stacks_list2[from_stack][-how_many_to_move:]
    for item in moving_items:
        stacks_list2[to_stack].append(item)

text_answer2 = ""
for stack in stacks_list2:
    text_answer2 += stack[-1].rstrip("]").lstrip("[")
print(f"Answer part 2 : {text_answer2}\n")
