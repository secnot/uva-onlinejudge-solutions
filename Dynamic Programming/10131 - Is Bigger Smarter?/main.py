import sys
from itertools import count


def readnum():
    return list(map(int, sys.stdin.readline().split()))


def readcase():
    elephants = []
    num = count(1)
    while True:
        el = readnum()
        if not el:
            break
        weight, iq = el
        elephants.append((weight, iq, next(num)))

    return elephants


def sort_key(elephant):
    weight, iq, num = elephant
    return weight*10000-iq


def find_sequence(elephants):
    """Find longest sequence of elephants satisfying the problem condition"""
    # Sort descending weight, and increasing iq
    seq = sorted(elephants, reverse=True, key=sort_key)

    # seq_len contains the length for longest sequence reachable from each position
    seq_len = [1 for _ in seq]

    # seq_nxt 'points' to the position of the next element in the largest sequence
    seq_nxt = [n for n, _ in enumerate(seq)]

    # Iterate from the end to the start of the list building the longest sequences
    for c in range(1, len(seq)):
        current_weight, current_iq, _ = seq[c] # Current elephant

        for j in range(c-1, -1, -1):
            weight, iq, _ = seq[j]
            # Check iq is in of sequence
            if iq >= current_iq:
                continue

            # Same weight, if the sequence is larger than current copy it
            if current_weight == weight:
                # If the sequence is larger than current copy it
                if seq_len[j] > seq_len[c]:
                    seq_len[c] = seq_len[j]
                    seq_nxt[c] = seq_nxt[j]

            # Smaller weight, add sequence to current if it is longer
            else:
                if seq_len[j] >= seq_len[c]:
                    seq_len[c] = seq_len[j]+1
                    seq_nxt[c] = j

    # Find the starting position of the longest sequence
    _, start = max((s, n) for n,s in enumerate(seq_len))

    # Reconstruct sequence (using ordered seq indexes)
    longest = [start]
    while seq_nxt[longest[-1]]!=longest[-1]:
        longest.append(seq_nxt[longest[-1]])

    # Substitute sequence positions by original elephant numbers
    return [seq[e][2] for e in longest]


if __name__ == '__main__':
    elephants = readcase()
    seq = find_sequence(elephants)
    print(len(seq))
    for e in seq:
        print(e)
