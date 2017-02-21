from sys import stdin

# Solved using built-in big ints easy and SLOW,

REVMUL = [
    [], #0
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #1
    [], #2
    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3], #3
    [], #4
    [], #5 
    [], #6
    [0, 3, 6, 9, 2, 5, 8, 1, 4, 7], #7
    [], #8
    [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]] #9


def generate_ones_table(length):
    """Generate set to check if all number digits are ones"""
    table = set()
    prev=1
    for i in range(1,length):
        table.add(prev)
        prev=prev*10+1
    return table

ALLTHEONES = generate_ones_table(9000)



def digit(num, pos): # Returns digit pos in num
    return num//10**pos%10


def all_ones(num):
    return num in ALLTHEONES


def find_ones(num):

    last_digit = digit(num, 0)
    revmul = REVMUL[last_digit]

    prev = 0 # result of previous multiplication
    mult = 0 # multiplier used previous multiplication
    i = 0 # index of digit being 'fixed'

    while i==0 or not all_ones(prev):
        fix = digit(prev, i)
        mult = mult + revmul[(11-fix)%10]*(10**i)
        i += 1
        prev = num*mult

    return len(str(prev))


if __name__ == '__main__':
    while True:
        try:
            num = int(stdin.readline())
        except Exception:
            break

        print(find_ones(num))
