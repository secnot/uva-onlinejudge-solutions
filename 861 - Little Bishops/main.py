import sys





def load_case():
    return list(map(int, sys.stdin.readline().split()))



class Board(object):

    def __init__(self, n, b):
        self._n = n # Board size 
        self._b = b # bishops to place
        self._solutions_found = 0
        self._board = [0]*(self._n*self._n)
        self._moves = []

    def _mod_diagonals(self, k, v):
        x = k%self._n
        y = k//self._n

        for i in range(1, self._n - max(x, y)):
            self._board[k+(self._n+1)*i] += v
        for i in range(1, self._n - max(self._n-1-x, y)):
            self._board[k+(self._n-1)*i] += v

    def _make_move(self, k):
        self._board[k] += 9999
        self._moves.append(k)
        self._mod_diagonals(k, 1)

    def _undo_move(self):
        k = self._moves.pop()
        self._mod_diagonals(k, -1)
        self._board[k] = 0

    def _build_candidates(self, k):
        return [i for i in  range(k, self._n*self._n) if not self._board[i]]
    
    def _is_solved(self):
        return len(self._moves) >= self._b
        
    def _count_solutions(self, k=0):
        if self._is_solved():
            self._solutions_found += 1
            return

        candidates = self._build_candidates(k)
        for c in candidates:
            self._make_move(c)
            self._count_solutions(c+1)
            self._undo_move()

    def solutions(self):
        self._count_solutions()
        return self._solutions_found

if __name__ == '__main__':
    
    n, k = load_case()    
    while n:
        b = Board(n, k)
        b.solutions()
        print(b._solutions_found)
        n, k = load_case()
        if not n:
            break


