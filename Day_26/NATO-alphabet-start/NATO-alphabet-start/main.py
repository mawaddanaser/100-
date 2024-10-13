student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data_frame)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_list = [nato_dic[letter] for letter in word]
print(word_list)