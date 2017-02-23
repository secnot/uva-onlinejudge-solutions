from sys import stdin



def readnum():
    line = stdin.readline()
    if not line:
        return None, None
    return [int(x) for x in line.split()]


def num_expressions(pairs, depth, mem):
    """
    This problem can be solved using recursion + memoization, but the recursion
    used is more complex that I thought, it's based on on catalan numbers:
    
    https://en.wikipedia.org/wiki/Catalan_number
   
    which appear in many recursive problems it seems.... it's even one of the examples


    for 0 <= k <= n - 1
    N(n，d） = N（0，d-1）*N（n-1，d）+ N（1，d-1）*N（n-2，d）+ …… +
                N（k，d-1）*N（n-k-1，d)

    Many time wasted had too search for a solution....
    """
    if (pairs, depth) in mem:
        return mem[pairs, depth]
    if pairs == 0 or depth ==1:
        mem[pairs, depth] = 1
        return 1

    total = 0
    for i in range(pairs):
        total += num_expressions(i, depth - 1, mem) * \
            num_expressions(pairs - 1 - i, depth, mem)
    mem[pairs,depth] = total
    return total


if __name__ == '__main__':
    
    mem = {}
    while True:
        n, d = readnum()
        if not n:
            break
        
        nexp = num_expressions(n//2, d, mem) - num_expressions(n//2, d-1, mem)
        print(nexp)
