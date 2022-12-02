# task description: https://adventofcode.com/2022/day/2

with open("day2_input.txt", "r") as file:
    read_file = file.readlines()

my_hand = []
opponent_hand = []
score = 0
for line in read_file:
    splitted = line.strip().split(" ")
    my_hand.append(splitted[1])
    opponent_hand.append(splitted[0])

print(my_hand)
print(opponent_hand)

# part 1
for i in range(len(opponent_hand)):
    if my_hand[i] == "X":   # rock
        score += 1
        if opponent_hand[i] == "A":     # rock
            score += 3
        elif opponent_hand[i] == "B":   # paper
            score += 0
        elif opponent_hand[i] == "C":   # scissors
            score += 6
    elif my_hand[i] == "Y":     # paper
        score += 2
        if opponent_hand[i] == "A":     # rock
            score += 6
        elif opponent_hand[i] == "B":   # paper
            score += 3
        elif opponent_hand[i] == "C":   # scissors
            score += 0
    elif my_hand[i] == "Z":     # scissors
        score += 3
        if opponent_hand[i] == "A":     # rock
            score += 0
        elif opponent_hand[i] == "B":   # paper
            score += 6
        elif opponent_hand[i] == "C":   # scissors
            score += 3

print(f"Score part 1: {score}")

# part 2
score2 = 0
for i in range(len(opponent_hand)):
    if opponent_hand[i] == "A":   # rock
        if my_hand[i] == "X":   # lost
            score2 += 0  # for lost
            score2 += 3  # for scissors
        elif my_hand[i] == "Y":     # draw
            score2 += 3  # for draw
            score2 += 1  # for rock
        elif my_hand[i] == "Z":    # win
            score2 += 6  # for win
            score2 += 2  # for paper
    elif opponent_hand[i] == "B":   # paper
        if my_hand[i] == "X":   # lost
            score2 += 0  # for lost
            score2 += 1  # for rock
        elif my_hand[i] == "Y":     # draw
            score2 += 3  # for draw
            score2 += 2  # for paper
        elif my_hand[i] == "Z":    # win
            score2 += 6  # for win
            score2 += 3  # for scissors
    elif opponent_hand[i] == "C":   # scissors
        if my_hand[i] == "X":   # lost
            score2 += 0  # for lost
            score2 += 2  # for paper
        elif my_hand[i] == "Y":     # draw
            score2 += 3  # for draw
            score2 += 3  # for scissors
        elif my_hand[i] == "Z":    # win
            score2 += 6  # for win
            score2 += 1  # for rock
print(f"Score part 2: {score2}")
