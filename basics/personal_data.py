personal_data = "hcl:5d90f0 cid:270"
records = personal_data.split()

dict = {}

print(records)
# for data in records:
#     data = data.split(":")
#     dict[data[0]] = data[1]
#
# print(dict)


for record in records:
    key, value = record.split(":")
    dict[key] = value

print(dict)