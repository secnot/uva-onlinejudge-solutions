from sys import stdin

REVMUL = {
    1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    3: [0, 7, 4, 1, 8, 5, 2, 9, 6, 3],
    7: [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],
    9: [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]}

def generate_ones_table(length):
    return set([int("1"*i) for i in range(1, length)])

ALLTHEONES = generate_ones_table(20)

def digit(num, pos): # Returns digit pos in num
    return num//10**pos%10

def all_ones(num):
    return num in ALLTHEONES

def find_ones(num):

    if all_ones(num):
        return len(str(num))

    revmul = REVMUL[digit(num, 0)]

    prod = 0 # rest previous multiplication not 
    length = 0 # number of 1 computed

    while not all_ones(prod):
        first = digit(prod, 0)
        prod = prod + num*revmul[(11-first)%10]
        prod = prod//10 # discard last digit (it's a one)
        length += 1
    
    return length+len(str(prod))


if __name__ == '__main__':
    while True:
        try:
            num = int(stdin.readline())
        except Exception:
            break

        print(find_ones(num))
