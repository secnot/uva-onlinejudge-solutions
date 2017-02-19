import sys


def read_num():
    line = sys.stdin.readline()
    return list(map(int, line.rstrip().split()))


def sum_distances(house, relatives):
    return sum(abs(r-house) for r in relatives)


def optimal_house(relatives, numbers):
    s = sorted(numbers)
    return s[len(s)//2]


if __name__ == '__main__':
    
    tests = read_num()[0]

    for i in range(tests):
        test = read_num()
        relatives = test[0]
        numbers = test[1:]

        house = optimal_house(relatives, numbers)
        print(sum_distances(house, numbers))
    
    exit(0)
