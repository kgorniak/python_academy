with open("input.txt", "r") as file:
    read_file = file.readlines()

data_list = []
for line in read_file:
    raw_data = line.split(" ")
    for data in raw_data:
        data_list.append(data)

# print(data_list)
persons_list = []
data_dict = {}
for data in data_list:
    if data != "\n":
        splitted = data.split(":")
        data_dict[splitted[0]] = splitted[1]
    elif data == "\n":
        persons_list.append(data_dict)
        data_dict = {}

print(len(persons_list))
print(persons_list)