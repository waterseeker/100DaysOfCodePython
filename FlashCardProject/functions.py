import pandas as pd


# make word list from x words from the csv
def get_word_list(number_of_words):
    # read csv as pandas df
    words = pd.read_csv("data/finnish_words.csv")
    # get a df of number_of_words in length
    word_list = words.head(number_of_words)
    return word_list


# get next word from word list
