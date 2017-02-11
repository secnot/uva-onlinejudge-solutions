import sys
from copy import copy

def load_num():
    line = sys.stdin.readline()
    if line == '' or line == '\n':
        return None

    return list(map(int, line.rstrip().split()))

def find_pos(lst, element):
    """Find position of element in list"""
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return None

def iflip(stack, pos):
    """inplace flip"""
    if pos >len(stack) or pos <1:
        raise ValueError

    for i, j in zip(range(pos-1, len(stack)), range(len(stack)-1, pos-1, -1)):
        if i>=j:
            break
        stack[i], stack[j] = stack[j], stack[i]

def flip_sort(stack):
    """
    While not in order:
        1 - find biggest pancake not in position
        2 - flip it to the top of the stack (if not already in it)
        3 - flip the top of the stack into pancake correct positon
    """
    flips = []
  
    # Sorted stack
    sstack = sorted(stack, reverse = True)
    
    # Copy original stack
    stack = list(stack[::-1])

    # Sort
    for i in range(len(stack)-1):
        if stack[i] == sstack[i]:
            continue

        # Search elemenet position
        pos = find_pos(stack, sstack[i])
        
        # If element not on top flip to the top
        if pos != len(stack)-1:
            flips.append(pos+1)
            iflip(stack, pos+1)
        
        # Flip from top to correct position
        flips.append(i+1)
        iflip(stack, i+1)
   
    return flips

if __name__ == '__main__':

    while True:
        stack = load_num()
        if not stack:
            break
       
        print(" ".join(map(str, stack)))
        solution = flip_sort(stack)
        
        if solution:
            print(" ".join(map(str, solution+[0])))
        else:
            print(0)

    exit(0)
