import sys
from collections import defaultdict
from copy import copy
import string

ALPHABET = string.ascii_lowercase

def load_num():
    return int(sys.stdin.readline().rstrip())


def valid_sub(enc, word, subs):
    
    if len(enc) != len(word):
        return False

    for e, w in zip(enc, word):
        if subs[e] and subs[e]!=w: 
            return False

    return True


def create_sub(enc, word, subs):
    new_subs = copy(subs)

    for e, w in zip(enc, word):
        if new_subs[e] == w:
            continue

        if new_subs[e] is not None:
            raise ValueError

        # No two letters can be reblaced by same letter
        if w in new_subs.values():
            raise ValueError
        new_subs[e] = w
    
    return new_subs


def decrypt(enc, words, subs=None):
    """Recursive solution using backtracking"""

    if subs is None:
        subs = {c: None for c in ALPHABET}

    for word in words[len(enc[0])]:
        # Check word  is valid with current substitutions
        if not valid_sub(enc[0], word, subs):
            continue

        # Create new substitution dict for the word
        try:
            new_subs = create_sub(enc[0], word, subs)
        except ValueError:
            continue
 
        # This is the end of the search
        if len(enc) == 1:
            return [word]
        
        # More words in the list .. keep searching
        dec = decrypt(enc[1:], words, new_subs)
        if dec is not None:
            return [word]+dec
        
    return None




if __name__ == '__main__':
    nwords = load_num()
    
    words = defaultdict(list)
    for _ in range(nwords):
        word = sys.stdin.readline().rstrip().lower()
        words[len(word)].append(word)

    for enc in sys.stdin:
        enc = enc.split()
        if len(enc) == 0:
            break

        dec = decrypt(enc, words)
        if dec:
            print(' '.join(dec))
        else:        
            print(' '.join("*"*len(w) for w in enc))

