with open("List_coprehensions/file1.txt", "r") as file1:
    f = file1.read().splitlines()
    f1 = [int(i) for i in f]


with open("List_coprehensions/file2.txt", "r") as file2:
    f = file2.read().splitlines()
    f2 = [int(i) for i in f]

result = [same for same in f1 if same in f2]
print(result)
