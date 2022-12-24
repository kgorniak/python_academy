# task description: https://adventofcode.com/2022/day/6
four_char_list = []


def get_four_characters(start, end):

    for counter in range(start, end):
        four_char_list.append(read_file[counter])
    print(four_char_list)
    return four_char_list


def compare_chars(chars_list):
    for index in range(len(chars_list)):
        if chars_list[index] == chars_list[index + 1]:
            return False
        else:
            return True


with open("day6_input.txt", "r") as file:
    read_file = file.readline()
    # get_four_characters(0, 4)
    if compare_chars(get_four_characters(0, 4)):
        print("True")
