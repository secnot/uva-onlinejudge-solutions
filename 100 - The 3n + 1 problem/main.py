import sys
import functools


@functools.lru_cache(None)
def cycle_length(start):
    count = 1

    n = start
    while n != 1:
        count += 1
        if n%2 ==1:
            n = 3*n+1
        else:
            n = n//2
  
    return count


@functools.lru_cache(None)
def max_cycle(start, end):
    start, end = min(start, end), max(start, end)
    return max(cycle_length(n) for n in range(start, end+1))


if __name__ == '__main__':

    for line in sys.stdin:
        start, end = map(int, line.split()[:2])
        print(start, end, max_cycle(start, end))

    exit(0)
