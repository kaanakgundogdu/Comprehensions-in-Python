student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato_df.iterrows()}

user_input = input(f"Type a word: ")

for i in user_input:
    print(f"{nato_dict[i.upper()]} for {i.upper()}")
