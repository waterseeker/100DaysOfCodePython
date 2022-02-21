import pandas as pd
import random


# make word list from x words from the csv
def get_word_list(number_of_words):
    # read csv as pandas df
    words = pd.read_csv("data/finnish_words.csv")
    # get a df of number_of_words in length
    words_head = words.head(number_of_words)
    words_dictionary = words_head.to_dict(orient="records")
    return words_dictionary


# get random word from word dictionary
def get_random_word(word_dictionary):
    word_data = random.choice(word_dictionary)
    return word_data
