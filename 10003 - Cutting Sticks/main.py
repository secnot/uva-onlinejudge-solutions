from sys import stdin

# TODO: Too slow for now see main.c

def readstick():
    """Read one stick problem form stdin"""
    length = int(stdin.readline())
    if not length:
        return None, None

    ncuts = int(stdin.readline())

    cuts = list(map(int, stdin.readline().split()))

    return length, cuts


def cost(s, e, cuts, mem):
    """Minimal cost of cuts from s to e
    Arguments: start, end, cuts, mem"""
    if (s,e) in mem:
        return mem[s, e]

    # Didn't have the cost stored, compute and store
    best = min(cost(s, i, cuts, mem)+cost(i, e, cuts, mem) for i in range(s+1, e))
    mem[s, e] = best + cuts[e]-cuts[s]
    return mem[s,e]
    

def min_cost(length, cuts):
    """Find minimum cost using recursion with memoization""" 
    cuts = [0] + cuts + [length]

    # Cost table
    mem = {}
    for c in range(len(cuts)-1):
        mem[c, c+1] = 0

    return cost(0, len(cuts)-1, cuts, mem)
       

if __name__ == '__main__':
    
    length, cuts = readstick()
    while length:
        print('The minimum cutting is {}.'.format(min_cost(length, cuts)))
        length, cuts = readstick()
