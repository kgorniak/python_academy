# x.strip()
# x.split(a)
# x.replace(a,b)
# “ ”.join()


text = "andrzej testowy"

# text_list = text.split()
# name = text[0].capitalize()
# surname = text[1].capitalize()
#
# print(f"Name = {name}\nSurname = {surname}")

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels_count = 0
for i in text:
    if i in vowels:
        vowels_count += 1
print(vowels_count)
