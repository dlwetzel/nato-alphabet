import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)

user_word = input("enter a word: ").upper()
nato_code = []
for character in user_word:
    nato_code.append(data_dict[character])

print(nato_code)
