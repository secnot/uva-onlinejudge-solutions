import sys
from copy import deepcopy
from math import sqrt


def read_num():
    return list(map(int, sys.stdin.readline().split()))

def read_sudoku():
    try:
        n = read_num()
        if not n:
            n = read_num()
        n = n[0]
        return [read_num() for _ in range(n*n)]
    except Exception:
        return None

def print_sudoku(s):
    for l in s:
        print(" ".join(map(str, l)))


class Sudoku(object):

    def __init__(self, board):
        # cell size
        self._dim = int(sqrt(len(board)))

        # Remaining open spaces
        self._nfree = sum(1 for l in board for i in l if not i)
      
        # Moved made
        self._moves = []
        self._board = deepcopy(board)

    def _undo_move(self):
        x, y = self._moves.pop()
        self._board[x][y] = 0
        self._nfree += 1

    def _make_move(self, x, y, value):
        self._moves.append((x, y))
        self._board[x][y] = value
        self._nfree -= 1

    def _possible_values(self, x, y):
        # Horizontal restrictions
        h = self._board[x] 

        # Vertical restrictions
        v = [self._board[i][y] for i in range(len(self._board))]
        
        # Square restrictions
        square_x, square_y = (x//self._dim)*self._dim, (y//self._dim)*self._dim
        s = [self._board[square_x+i][square_y+j] 
                for i in range(self._dim)
                for j in range(self._dim)]

        # Return values not present in any restriction
        restrictions = set(h+v+s)
        return [x for x in range(1, len(self._board)+1) if x not in restrictions]

    def _construct_candidates(self):
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if not self._board[i][j]:
                    return [(i, j, v) for v in self._possible_values(i, j)]
        return []

    def is_solved(self):
        return not bool(self._nfree)

    def solve(self):
        if self.is_solved():
            return

        candidates = self._construct_candidates()
        for c in candidates:
            self._make_move(*c)
            self.solve() 
            if self.is_solved():
                return
            self._undo_move()

    def print(self):
        if self.is_solved():
            print_sudoku(self._board)
        else:
            print('NO SOLUTION')


if __name__ == '__main__':
    sudoku = read_sudoku()
    while sudoku:
        su = Sudoku(sudoku)
        su.solve()
        su.print()
        
        sudoku = read_sudoku()
        if sudoku:
            print('')
