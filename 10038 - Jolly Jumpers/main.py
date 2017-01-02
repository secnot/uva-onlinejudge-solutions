import sys

def load_nums():
    num_str = sys.stdin.readline()
    if num_str == '\n' or num_str=='':
        return None

    return list(map(int, num_str.rstrip().split()))


def is_jolly(numbers):
    
    sub = set([abs(b-a) for a, b in zip(numbers, numbers[1:])])
   
    for n in range(1, len(numbers)):
        if n not in sub:
            return False

    return True


if __name__ == '__main__':

    while True:
        numbers = load_nums()
        if numbers is None:
            break

        if is_jolly(numbers[1:]):
            print("Jolly")
        else:
            print("Not jolly")

