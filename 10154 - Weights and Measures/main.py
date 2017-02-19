import sys
import operator

def readturtles():
    return [tuple(map(int, line.split())) for line in sys.stdin]

def stack_all_the_turtles(turtles):
    """Find tallest stack using LIS longest increasing subsequence"""
    turtles = sorted(turtles, key=operator.itemgetter(1))

    lis = [float("inf") for _ in turtles]
    lis[0], longest_seq = 0, 0

    for t_weight, t_strength in turtles:
        for j in range(longest_seq, -1, -1):
            if t_strength > lis[j]+t_weight and t_weight + lis[j] < lis[j+1]:
                lis[j+1] = lis[j]+t_weight
                longest_seq = max(longest_seq, j+1)

    return longest_seq

if __name__ == '__main__':
    print(stack_all_the_turtles(readturtles()))
