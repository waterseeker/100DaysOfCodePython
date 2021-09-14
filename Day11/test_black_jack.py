from collections import Counter

cards = [11, 11, 11, 11, 11, 11]


def get_score(hand_array):
    # is it blackjack?
    if len(hand_array) == 2:
        if sum(hand_array) == 21:
            return 'blackjack'
    number_of_aces = Counter(hand_array)[11]
    non_ace_total = sum(card for card in hand_array if card != 11)
    if number_of_aces > 0:
        if non_ace_total + 11 + (number_of_aces - 1) <= 21:
            ace_value = 11 + (number_of_aces - 1)
        else:
            ace_value = number_of_aces
    hand_total = non_ace_total + ace_value
    return hand_total


print(get_score(cards))
