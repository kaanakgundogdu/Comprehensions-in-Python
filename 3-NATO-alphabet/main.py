import pandas
student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato_df.iterrows()}


def generate_phonetic():
    user_input = input(f"Type a word: ")
    try:
        output_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
