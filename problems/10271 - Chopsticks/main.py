from sys import stdin
from collections import defaultdict

# THIS IMPLEMENTATION IS STILL TOO SLOW USING PYTHON, A C IMPLEMENTATION
# IS PROVIDED (main.c)


INFINITE = 9999999999


def readnum():
    return list(map(int, stdin.readline().split()))


def readcase():
    Kits, N = readnum()
    Chopsticks = readnum()
    return  Kits+8, Chopsticks


def build_kits_mem(sticks, badness, s, k, mem):   
    if (s, k) in mem:
        return mem[k, s]

    if s < 3*k:
        mem[k, s] = float('inf')
    elif k==0:
        mem[k, s] = 0
    else:
        mem[k, s] = min(
            build_kits_mem(sticks, badness, s-1, k, mem), # Third chopstic
            build_kits_mem(sticks, badness, s-2, k-1, mem)+badness[s]) # Pair
    return mem[k, s]


def build_kits(sticks, nkits):
    """Recursive with memoization, left for clarity sake as the precursor of 
    the table implementations, 
    (WARNING: will fail if recursion limit is reached)"""
    sticks = sorted(sticks, reverse=True)
    badness = [0 for _ in range(len(sticks)+3)]

    for i in range(1, len(sticks)):
        badness[i+1] = (sticks[i]-sticks[i-1])**2
        
    mem = defaultdict(lambda: -1)
    return build_kits_mem(sticks, badness, len(sticks), nkits, mem)


def build_kits_table(sticks, kits):
    """Table implementation"""
    sticks = sticks[::-1]
    badness = [0 for _ in range(len(sticks)+3)]

    for i in range(1, len(sticks)):
        badness[i+1] = (sticks[i]-sticks[i-1])**2
       
    dp = [[-1 for _ in range(len(sticks)+1)] for _ in range(kits+1)]
    dp[0] =[0 for _ in dp[0]]

    for k in range(1, kits+1):
        dp[k][3*k-1] = INFINITE
        for s in range(3*k, len(sticks)+1):
            dp[k][s] = min(dp[k][s-1], dp[k-1][s-2]+badness[s])
    
    return dp[kits][len(sticks)]


def build_kits_table_fast(sticks, kits):
    """The same as table implementation but only using the last two rows 
    of DP array, and some other minor optimizations"""
    sticks = sticks[::-1]
    badness = [0 for _ in range(len(sticks)+3)]

    for i in range(1, len(sticks)):
        badness[i+1] = (sticks[i]-sticks[i-1])**2

    prev = [0 for _ in range(len(sticks)+1)]
    current = [-1 for _ in range(len(sticks)+1)]

    for k in range(1, kits+1):
        current[3*k-1] = INFINITE
        for s in range(3*k, len(sticks)-abs(k-kits)*2+1):
            if current[s-1] <= prev[s-2]+badness[s]:
                current[s] = current[s-1]
            else:
                current[s] = prev[s-2]+badness[s]
        prev, current = current, prev
    
    return prev[len(sticks)]


if __name__ == '__main__':

    ncases = int(stdin.readline())

    for  c in range(ncases):
        Kits, Chopsticks = readcase()
        print(build_kits_table_fast(Chopsticks, Kits))
        
