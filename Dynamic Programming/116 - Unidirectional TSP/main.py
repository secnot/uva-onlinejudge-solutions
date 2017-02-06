import sys


def readnum():
    return list(map(int, sys.stdin.readline().split()))


def readmatrix():
    try:
        rows, columns = readnum()
    except ValueError:
        return []   # EOF

    # Read all matrix integers into a single list
    integers = []
    while len(integers) < rows*columns:
        integers.extend(readnum())

    # Reconstruct matrix
    return [integers[columns*r:columns*(r+1)] for r in range(rows)]


def best_path(matrix):
    nrows = len(matrix)
    ncolumns = len(matrix[0])

    # Shortest Path -> each cell contains weight for the minimal path
    # to reach the cell followed by the list of rows used by the path.
    sp = [[None for _ in range(ncolumns)] for _  in range(nrows)]
    for r in range(nrows): # Initialize first column
        sp[r][0] = (matrix[r][0], r+1)
  
    # Construct minimal weight matrix
    for c in range(1, ncolumns):
        for r in range(nrows):

            # Cells from previous column from where this cell can be reached 
            # (wrapping first and last rows)
            top = sp[(nrows+r-1)%nrows][c-1]
            mid = sp[r][c-1]
            bot = sp[(r+1)%nrows][c-1]

            # best path to reach this cell
            best = min(top, mid, bot)
            
            # Add current cell weight to the path weight, and append current row
            sp[r][c] = (best[0] + matrix[r][c],) + best[1:] + (r+1,)

    # Find minimal-weight path
    min_path = min(sp[r][-1] for r in range(nrows))
    
    return min_path[0], min_path[1:]


if __name__ == '__main__':
    
    matrix = readmatrix()
    while matrix:
        cost, path = best_path(matrix)
        print(" ".join(map(str, path)))
        print(cost)
        matrix = readmatrix()
