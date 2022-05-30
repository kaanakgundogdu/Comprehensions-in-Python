numbers = [1, 2, 3]

# old way
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List comprehension

new_list = [n + 1 for n in numbers]

print(new_list)

name = "Kaan"
letters = [n for n in name]
print(letters)

new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ["Kaan", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [n.upper() for n in names if len(n) >= 5]
print(short_names)
