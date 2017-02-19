from sys import stdin

CARD_SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def readnum():
    return list(map(int, stdin.readline().split()))

def readcase():
    nshuffles = int(stdin.readline())
   
    # Read all shuffles into a single list and then split them, because
    # a shuffle could extend more than one line
    all_shuffles = []
    while len(all_shuffles)<nshuffles*52:
        all_shuffles.extend(readnum())

    shuffles = []
    for i in range(nshuffles):
        shuffles.append(all_shuffles[i*52:(i+1)*52])

    # Read shuffles observed
    observed = []
    while True:
        try:
            seen = int(stdin.readline())
            observed.append(seen)
        except Exception:
            break   #Found empty line

    return shuffles, observed


def card_to_str(card):
    card = card - 1
    suit = card//13
    value = card%13
    return CARD_VALUES[value]+' of '+CARD_SUITS[suit]

def print_deck(deck):
    for c in deck:
        print(card_to_str(c))

def apply_shuffle(deck, shuffle):
    sdeck = list(deck)
    
    for dest, pos in enumerate(shuffle):
        sdeck[dest] = deck[pos-1] 

    return sdeck

def shuffle_deck(shuffles, observed):
  
    # Create initial ordered deck
    deck = list(range(1, 53))
   
    # Apply observed.shuffles
    for s in observed:
        deck = apply_shuffle(deck, shuffles[s-1])

    return deck

if __name__ == '__main__':
    
    ncases = int(stdin.readline())
    empty_line = stdin.readline()

    for c in range(ncases):
        shuffles, observed = readcase()
        deck = shuffle_deck(shuffles, observed)
        print_deck(deck)
        if c+1 < ncases:
            print('')
