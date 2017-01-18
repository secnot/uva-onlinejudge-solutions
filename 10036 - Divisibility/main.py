import sys

def load_num():
    return list(map(int, sys.stdin.readline().split()))

def load_case():
    _, divisor = load_num()
    numbers = load_num()
    return numbers, divisor

def is_divisible(num, k):
    n = len(num)

    rem = [[False]*k for _ in range(n)]
    rem[0][num[0]%k] = True

    for i in range(1, n):
        for j in range(k):
            if rem[i-1][j]:
                rem[i][(j+num[i])%k] = True
                rem[i][(j+k-num[i])%k] = True

    return rem[n-1][0]

if __name__ == '__main__':    
    for c in range(load_num()[0]):
        if is_divisible(*load_case()):
            print('Divisible')
        else:
            print('Not divisible')
