import pandas as pd

# getting just the words for the first 1000 words
with open("finnish_words.txt", "r") as file:
    word_list = [line.split()[0] for line in file.readlines()][:1000]

# with open("first_1000_finnish_words.txt", "w") as file:
#     file.writelines(word_list)
df = pd.read_table("finnish_words.txt", delim_whitespace=True, names=("word", "frequency"))
print(df.head())
