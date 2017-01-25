import sys
from copy import copy


MANHATTAN_DST = [ 
    [0, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5,],
    [0, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4,],
    [0, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 5, 4, 3,],
    [0, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4,],
    
    [0, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4,],
    [0, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3,],
    [0, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2,],
    [0, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3,],

    [0, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3,],
    [0, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2,],
    [0, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1,],
    [0, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2,],

    [0, 3, 4, 5, 6, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2,],
    [0, 4, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1,],
    [0, 5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0,],
    [0, 6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1,]]



def manhattan_dist(puzzle):
    return sum(MANHATTAN_DST[p][v] for p, v in enumerate(puzzle))

def move_up(puzzle):
    pos = puzzle.index(0)
    puzzle[pos], puzzle[pos-4] = puzzle[pos-4], puzzle[pos]
    return True

def move_down(puzzle):
    pos = puzzle.index(0)
    puzzle[pos], puzzle[pos+4] = puzzle[pos+4], puzzle[pos]
    return True

def move_left(puzzle):
    pos = puzzle.index(0)
    puzzle[pos], puzzle[pos-1] = puzzle[pos-1], puzzle[pos]
    return True

def move_right(puzzle):
    pos = puzzle.index(0)
    puzzle[pos], puzzle[pos+1] = puzzle[pos+1], puzzle[pos]
    return True

def is_solved(puzzle):
    #return manhattan_dist(puzzle) == 0
    return all(i==j for i, j in zip(puzzle, range(1, 16)))

def load_num():
    return list(map(int, sys.stdin.readline().split()))

def read_puzzle():
    return load_num() + load_num() + load_num() + load_num()


def nr_of_inversions(puzzle):
    result = 0

    for i in  range(16):
        for j in range(i+1, 16):
            if (puzzle[i] == 0 or puzzle[j] == 0):
                continue

            if (puzzle[i] > puzzle[j]):
                result += 1

    return result

def is_solvable(puzzle):
    pos = puzzle.index(0)
    count = nr_of_inversions(puzzle)

    if ((4 - pos//4) % 2 == 0):
        return count % 2 == 1
    else:
        return count % 2 == 0

  


class PuzzleSolver(object):
    
    def __init__(self, limit=50, heuristic=manhattan_dist):
        self._heuristic = heuristic
        self._limit = limit

    def _make_move(self, move):
        if move == 'D':
            move_down(self._puzzle)
        elif move == 'U':
            move_up(self._puzzle)
        elif move == 'R':
            move_right(self._puzzle)
        elif move == 'L':
            move_left(self._puzzle)

        self._moves.append(move)

    def _undo_move(self):
        if self._moves[-1] == 'D':
            move_up(self._puzzle)
        elif self._moves[-1] == 'U':
            move_down(self._puzzle)
        elif self._moves[-1] == 'R':
            move_left(self._puzzle)
        elif self._moves[-1] == 'L':
            move_right(self._puzzle)

        self._moves.pop()

    def _valid_moves(self):
        pos = self._puzzle.index(0)
        candidates = []

        if self._moves:
            last_move = self._moves[-1]
        else:
            last_move = 'N'
       
        # Up
        if last_move != 'D' and pos//4!=0:
            candidates.append('U')
        
        # Down
        if last_move != 'U' and pos//4!=3:
            candidates.append('D')
        
        # Left
        if last_move != 'R' and pos%4!=0:
            candidates.append('L')
        
        # Right
        if last_move != 'L' and pos%4!=3:
            candidates.append('R')

        return candidates

    def _depth(self, max_cost):
        candidates = self._valid_moves()

        for move in candidates:
            self._make_move(move)
            h = self._heuristic(self._puzzle)
            if h == 0:
                self._solved = True
                return
            
            cost = h + len(self._moves) + 1
            if cost <= max_cost:
                self._depth(max_cost)
                if self._solved:
                    return
            self._undo_move()


    def solve(self, puzzle):

        if is_solved(puzzle):
            return []

        if not is_solvable(puzzle):
            return None

        max_cost = self._heuristic(puzzle)

        while(max_cost <= self._limit):
            self._puzzle = copy(puzzle)
            self._moves = []
            self._solved = False
            
            self._depth(max_cost)

            if self._solved:
                return self._moves
            else:
                max_cost += 5
        
        return None


def test_solution(puzzle, solution):

    puzzle=copy(puzzle)
    
    for i, move in enumerate(solution):
        if move == 'D':
            move_down(puzzle)
        elif move == 'U':
            move_up(puzzle)
        elif move == 'R':
            move_right(puzzle)
        elif move == 'L':
            move_left(puzzle)
        
    assert is_solved(puzzle)


if __name__ == '__main__':
   
    ncases = load_num()[0]

    p = PuzzleSolver(limit=50)
    for _ in range(ncases):
        puzzle = read_puzzle()
        solution = p.solve(puzzle)
        
        if solution is not None:
            print(''.join(solution))
            test_solution(puzzle, solution)
        else:
            print('This puzzle is not solvable.')
