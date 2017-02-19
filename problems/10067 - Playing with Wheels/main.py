import sys
import operator
from collections import deque

def add_wo_carry(n1, n2):
    """
    Add two integer strings of same length without carry
    >>> add_wo_carry('9876', '5432')
    '0008'
    """
    l1 = [int(x) for x in str(n1)]
    l2 = [int(x) for x in str(n2)] 
    res1 = map(operator.add, l1, l2)
    res2 = [str(x)[-1] for x in res1]
    return "".join(res2)

def sub_wo_carry(n1, n2):
    """
    Substract two integer strings of same length without carry
    >>> sub_wo_carry('9007', '1234')
    '8873'
    """
    l1 = [int(x)+10 for x in str(n1)]
    l2 = [int(x) for x in str(n2)] 
    res1 = map(operator.sub, l1, l2)
    res2 = [str(x)[-1] for x in res1]
    return "".join(res2)

def neighbours(num):
    """List of numbers reachable from num with only one button press
    >>> neighbours('0234')
    ['0235', '0244', '0334', '1234', '0233', '0224', '0134', '9234']
    """
    num = str(num)
    num = '0'*(4-len(num))+num # Prepend 0 until length is 4

    return [
        int(add_wo_carry(num, '0001')),
        int(add_wo_carry(num, '0010')),
        int(add_wo_carry(num, '0100')),
        int(add_wo_carry(num, '1000')),
        int(sub_wo_carry(num, '0001')),
        int(sub_wo_carry(num, '0010')),
        int(sub_wo_carry(num, '0100')),
        int(sub_wo_carry(num, '1000'))]


adjList = [neighbours(v) for v in range(0, 10000)]


def button_presses(start, end, restrictions):
    """Find minimum number of button presses required to go from
    start to end without going through
    """
    if start == end:
        return 0

    if end in restrictions:
        return -1

    restrictions = set(restrictions)
    parent = [-1 for x in range(10000)]
    discovered = [False for x in range(10000)]
    processed =  [False for x in range(10000)]

    # Shortest path BFS
    q = deque([start])
    discovered[start]

    while q:
        v = q.popleft()
        processed[v] = True

        for n in adjList[v]:
            if not discovered[n] and not n in restrictions:
                q.append(n)
                discovered[n] = True
                parent[n] = v

    if parent[end] == -1:
        return -1

    # Find shortest path edges
    count = 0
    current = end
    while current != start:
        current = parent[current]
        count += 1

    return count


def load_num():
    num_str = sys.stdin.readline()
    if num_str == '\n':
        num_str = sys.stdin.readline()

    return int(num_str.replace(" ", "").rstrip())

def load_next_test():
    start = load_num()
    end = load_num()
    n_restrictions = load_num()
    
    restrictions = []
    for l in range(n_restrictions):
        restrictions.append(load_num())
    return start, end, restrictions

if __name__ == '__main__':

    test_number = load_num()

    for t in range(test_number):
        start, end, restrictions = load_next_test()
        print(button_presses(start, end, restrictions))

    exit(0)
