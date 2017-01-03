import sys

def load_num():
    num_str = ''
    while num_str == '\n' or num_str=='':
        num_str = sys.stdin.readline()

    return list(map(int, num_str.rstrip().split()))



def load_case():
    lines, length = load_num()
   
    grid = []
    for l in range(lines):
        grid.append(sys.stdin.readline().rstrip().lower())

    nwords = load_num()[0]
    words = []
    for l in range(nwords):
        words.append(sys.stdin.readline().rstrip().lower())

    return grid, words


def find_word(grid, word):
    operations = ((1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (-1, -1), (1, -1), (-1, 1))

    nlines = len(grid)
    ncolumns = len(grid[0])

    for l in range(0, nlines):
        for c in range(0, ncolumns):
            if grid[l][c] != word[0]:
                continue

            for op in operations:
                for letter in range(len(word)):
                    opc = c+op[0]*letter
                    opl = l+op[1]*letter
                    if opc<0 or opc>=ncolumns or opl<0 or opl>=nlines:
                        break
                    if grid[opl][opc] != word[letter]:
                        break
                else:
                    return (l, c)


def find_words(grid, words):
    return [find_word(grid, word) for word in words]

if __name__ == '__main__':
   
    cases = load_num()[0]

    for case in range(cases):
        positions = find_words(*load_case())
        for line, column in positions:
            print("{} {}".format(line+1, column+1))

        if case+1 < cases:
            print("")
        
