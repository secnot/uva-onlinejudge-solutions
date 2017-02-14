from sys import stdin
from collections import Counter

MAX_RANK = 1000000

CARD_SUITS = {'C': 1, 'D': 2, 'H': 3, 'S': 4}
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
            '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K':13, 'A': 14}


class Card(object):
    def __init__(self, value, suit):
        if isinstance(value, str):
            value = CARD_VALUES[value]
        if isinstance(suit, str):
            suit = CARD_SUITS[suit]
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.value==othe.value

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'Card({}, {})'.format(self.value, self.suit)


def readhand():
    """Read next hand into back a white hands"""
    both_hands = stdin.readline().split()
    if not both_hands:
        return None, None

    both_hands = [Card(v, s) for v, s in both_hands]
    
    black_hand, white_hand = both_hands[:5], both_hands[5:]
    
    return black_hand, white_hand


def split_hand(hand):
    """ 88833 -> [(8, 3), (3, 2)]"""
    counts = Counter(c.value for c in hand)
    split = [(value, count) for value, count in counts.items()]
    return sorted(split, key=lambda x: 100*x[1]+x[0], reverse=True)


def rank_split(split):
    acc = 0
    for value, count in split:
        acc *= 16
        acc += value

    return acc

def rank_value(hand):
    acc = 0
    for c in hand:
        acc *= 16
        acc += c.value

    return acc



def rank_straight_flush(hand, split):
    if rank_flush(hand, split):
        return rank_straight(hand, split)

def rank_four_kind(hand, split):
    if split[0][1] == 4:
        return split[0][0]

def rank_full_house(hand, split):  
    if split[0][1]==3 and split[1][1]==2:
        return split[0][0]

def rank_flush(hand, split):
    if all(card.suit == hand[0].suit for card in hand):
        return rank_value(hand)

def rank_straight(hand, split):   
    if hand[0].value==hand[1].value+1==hand[2].value+2==hand[3].value+3==hand[4].value+4:
        return split[0][0]

def rank_three_kind(hand, split):
    if split[0][1] == 3:
        return split[0][0]

def rank_two_pairs(hand, split):
    if split[0][1]==2 and split[1][1]==2:
        return rank_split(split)

def rank_pair(hand, split):
    if split[0][1] == 2:
        return rank_split(split)

def rank_higher(hand, split):
    return rank_split(split)

def rank_hand(hand): 
    hand = sorted(hand, reverse=True)
    split = split_hand(hand)

    rank_funcs = [rank_higher, rank_pair, rank_two_pairs, rank_three_kind, rank_straight,
            rank_flush, rank_full_house, rank_four_kind, rank_straight_flush]
  
    return max([(MAX_RANK*n)+func(hand, split) for n, func in enumerate(rank_funcs) 
        if func(hand, split) is not None])


def find_winner(black_hand, white_hand):

    black_rating = rank_hand(black_hand)
    white_rating = rank_hand(white_hand)
    if black_rating > white_rating:
        return "Black wins."
    elif black_rating < white_rating:
        return "White wins."
    else:
        return "Tie."

if __name__ == '__main__':

    black, white = readhand()
    while black and white:
        print(find_winner(black, white))

        black, white = readhand()


