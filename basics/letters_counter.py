text = "kajak"
unique_letters = []

for i in text:
    if i not in unique_letters:
        unique_letters.append(i)

print(unique_letters)

# solution 1
dictionary = {}
# for i in unique_letters:
#     dictionary[i] = text.count(i)
# print(dictionary)

# solution 2
for i in text:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
print(dictionary)
