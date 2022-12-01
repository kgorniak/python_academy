with open("text2.txt", "r") as file:
    read_file = file.readlines()

data_list = []
data_dict = {}
for line in read_file:
    raw_data = line.split()
    for data in raw_data:
        data_list.append(data)

# print(data_list)

for data in data_list:
    splitted = data.split(":")
    data_dict[splitted[0]] = splitted[1]

print(data_dict)
