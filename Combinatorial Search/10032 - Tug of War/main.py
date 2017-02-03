import sys

def load_num():
    return int(sys.stdin.readline().rstrip())

def load_case():
    _ = sys.stdin.readline() # Empty line
    npeople = load_num()
    return [load_num() for _ in range(npeople)]


def find_split(weights, total_weight):
    reachable = [0 for _ in range(total_weight+1)]
    reachable[0] = 1

    # If the bit k of the number stored in reachable[n] is active
    # that means that it is possible to select k out of all the
    # candidates, so the sum of their weight is n..
    # WARNING: Bitwise operations are too slow in python but it's still the 
    # fastest aproach.
    for i, w in enumerate(weights):
        for j in range(total_weight, -1, -1):
            if reachable[j]:
                reachable[j+w] |= (reachable[j]<<1)

    # Search nearest value to the perfect split reachable with the sum
    # of half of the weights
    half_weight = 0
    with_half_people = 1<<(len(weights)//2)
    for i in range(total_weight//2):
        if reachable[total_weight//2+i] & with_half_people:
            half_weight = total_weight//2+i
            break
        if reachable[total_weight//2-i] & with_half_people:
            half_weight = total_weight//2-i
            break

    return min(total_weight-half_weight, half_weight), max(total_weight-half_weight, half_weight)


def solve(weights):

    total_weight = sum(weights)
    
    # Check limit cases
    if len(weights) == 0:
        return 0, 0
    elif len(weights) == 1:
        return 0, weights[0]

    return find_split(weights, total_weight)


if __name__ == '__main__':

    ncases = load_num()
    
    for c in range(ncases):
        weights = load_case()
        low, high = solve(weights)
        print(low, high)
        if c+1 < ncases:
            print('')
