from sys import stdin


def readcase():
    return stdin.readline().rstrip(), stdin.readline().rstrip()


def nmatches_rec(txt, pat, t, p):
    """Find number of matches using simple recursion
        (will crash when recursion limit is reached)

        nmatches_rec(text, pattern, len(text), len(pattern))
    """
    if p==0:
        return 1

    if t==0:
        return 0

    matches = 0
    for i in range(t, 0, -1):
        if txt[t-i] == pat[p-1]:
            matches += nmatches_rec(txt, pat, t-i, p-1)

    return matches


def nmatches_mem(txt, pat, t, p, mem):
    """Find number of matches with recursion + memoization using a dictionary
        (this solution will also crash when recursion limit is reached)  
        
        nmatches_mem(text, pattern, len(text), len(pattern), {})
    """
    if (t,p) in mem:
        return mem[t, p]
    
    if p==0:
        return 1

    if t==0:
        return 0

    matches = 0
    for i in range(t, 0, -1):
        if txt[t-i] == pat[p-1]:
            matches += nmatches_mem(txt, pat, t-i, p-1, mem)

    mem[t, p] = matches
    return matches


def nmatches_table(txt, pat):
    """Find number or matches using table
    
        nmatches_table(text, pattern)
    """
    t, p = len(txt), len(pat)
    dp = [[0 for _ in range(t+1)] for _ in range(p+1)]
    for i in range(len(dp[0])):
        dp[0][i]=1
    
    for ip in range(p):
        matches = 0
        for it in range(ip, t):
            if txt[it] == pat[ip]:
                matches += dp[ip][it]
            dp[ip+1][it+1] = matches

    return max(dp[-1])


if __name__ == '__main__':
    
    ncases = int(stdin.readline())

    solutions = []
    for c in range(ncases):
        text, pattern = readcase()
        solutions.append(nmatches_table(text, pattern))
    print("\n".join(map(str, solutions)))
