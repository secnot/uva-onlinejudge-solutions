import sys
import operator


def readturtles():
    return [tuple(map(int, line.split())) for line in sys.stdin]

def stack_all_the_turtles(turtles):
    max_weight = max(s for _, s in turtles) # Heaviest stack possible
    turtles = sorted(turtles, key=operator.itemgetter(1))

    # tallest stack for given weight
    stacks = [0 for _ in range(max_weight+1)]
    stacks[0] = 1

    for turtle_weight, turtle_strength in turtles:

        for i in range(turtle_strength-turtle_weight, -1, -1):
            w, n = i, stacks[i] # Stack weight & number of turtles

            # If the current stack is taller than the one stored for this
            # weight update it
            if stacks[w+turtle_weight]<=n:
                stacks[w+turtle_weight] = n+1
    
    return max(stacks)-1

if __name__ == '__main__':
    print(stack_all_the_turtles(readturtles()))
