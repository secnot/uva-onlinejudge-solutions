import sys
from decimal import Decimal, getcontext

def load_num():
    num_str = ''
    while num_str == '\n' or num_str=='':
        num_str = sys.stdin.readline()

    return int(num_str.rstrip())


if __name__ == '__main__':
   
    # This problem is trivial using python's arbitrary precission integers.
    # A C implementation would require to roll your own integer system,
    # with a few operations, and use them to aproximate the solution with
    # a numerical method like bisection or newton
    # https://en.wikipedia.org/wiki/Root-finding_algorithm
    # https://en.wikipedia.org/wiki/Bisection_method
    # https://en.wikipedia.org/wiki/Newton%27s_method
    cases = load_num()
    
    getcontext().prec = 2000

    for c in range(cases):
        y = load_num()
        print(str(int(Decimal(y).sqrt())))

        if c+1 < cases:
            print('')

