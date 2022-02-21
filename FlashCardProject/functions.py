import pandas as pd
import random


# make word list from x words from the csv
def get_word_list(number_of_words):
    try:
        # read csv as pandas df
        words = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        words = pd.read_csv("data/finnish_words.csv")
    words_subset = words.head(number_of_words)
    words_to_learn = words_subset.to_dict(orient="records")
    return words_to_learn


# get random word from word dictionary
def get_random_word(word_dictionary):
    word_data = random.choice(word_dictionary)
    return word_data
