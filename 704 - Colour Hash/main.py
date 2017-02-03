import sys
from collections import deque

SOLUTION = (0, 3, 4, 3, 0, 5, 6, 5, 0, 1, 2, 1, 0, 7, 8, 7, 0, 9, 10, 9, 0)

CACHE_DEPTH = 8
MOVE_LIMIT = 16-CACHE_DEPTH

REVERSE_MOVE_TABLE = [0, 3, 4, 1, 2]


def readnum():
    return list(map(int, sys.stdin.readline().split()))

def readpuzzle():
    """Read and reorganize puzzle"""
    return readnum()[:21]

def left_clockwise(puzzle):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = puzzle
    return (p10, p11, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p12, p13, p14, p15, p16, p17, p18, p19, p20)

def left_counter_clockwise(puzzle):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = puzzle
    return (p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p0, p1, p12, p13, p14, p15, p16, p17, p18, p19, p20)

def right_clockwise(puzzle):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = puzzle
    return  (p0, p1, p2, p3, p4, p5, p6, p7, p8, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p9, p10)

def right_counter_clockwise(puzzle):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = puzzle
    return (p0, p1, p2, p3, p4, p5, p6, p7, p8, p19, p20, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)

def is_solved(puzzle):
    return puzzle==SOLUTION

def generate_candidates(puzzle, moves):
    candidates = []
    prev_move = moves[-1] if moves else 0
    
    if prev_move != 3:
        candidates.append( (left_clockwise(puzzle), moves+(1,)) )
    if prev_move != 4:
        candidates.append( (right_clockwise(puzzle), moves+(2,)) )
    if prev_move != 1:
        candidates.append( (left_counter_clockwise(puzzle), moves+(3,)) )
    if prev_move != 2:
        candidates.append( (right_counter_clockwise(puzzle), moves+(4,)) )

    return candidates





def store_in_cache(cache, puzzle, moves):
    if puzzle in cache and len(cache[puzzle]) <= len(moves):
        pass
    else:
        cache[puzzle] = moves

def generate_solution_cache(puzzle, depth):
    # Use DFS to generate all the positions reachable from puzzle with
    # up to to depth movements, and store the shortest sequence of movements 
    # to reach each one of those positions.
    cache = {}
    stack = generate_candidates(puzzle, ())

    while stack:
        puzzle, moves = stack.pop()
        store_in_cache(cache, puzzle, moves)
        if len(moves)<depth:
            stack.extend(generate_candidates(puzzle, moves))

    return cache


def reverse_moves(moves):
    return tuple(REVERSE_MOVE_TABLE[m] for m in moves)


def solve(cache, puzzle, moves=()):
    #TODO:  Use BFS to search...........
    if puzzle in cache:
        return list(moves)+list(reversed(reverse_moves(cache[puzzle])))

    fifo = deque(generate_candidates(puzzle, ()))

    while fifo:
        puzzle, moves = fifo.popleft()
        if puzzle in cache:
            return list(moves)+list(reversed(list(reverse_moves(cache[puzzle]))))
        if len(moves) <= MOVE_LIMIT:
            fifo.extend(generate_candidates(puzzle, moves))

    return None


if __name__ == '__main__':
    ncases = readnum()[0]
   
    cache = generate_solution_cache(SOLUTION, CACHE_DEPTH)

    for c in range(ncases):
        puzzle = tuple(readpuzzle())

        if is_solved(puzzle):
            print('PUZZLE ALREADY SOLVED')
        
        else:
            solution = solve(cache, puzzle)
            if not solution:
                print('NO SOLUTION WAS FOUND IN 16 STEPS')
            else:
                print("".join(map(str, solution)))
