# task description: https://adventofcode.com/2022/day/6

# part 1

def compare_chars(list):
    if len(list) == len(set(list)):
        return True


def get_four_chars(list, start, end):
    chars_list = list[start:end]
    return chars_list


with open("day6_input.txt", "r") as file:
    read_file = file.readline()
    print(read_file)

    start = 0
    end = 4
    for index, item in enumerate(read_file):
        four_list = get_four_chars(read_file, start, end)
        if compare_chars(four_list):
            print(four_list, index + 4)
            break
        else:
            start += 1
            end += 1

# part 2
# just change in lines 20 and 24 for '14' instead of '4'
