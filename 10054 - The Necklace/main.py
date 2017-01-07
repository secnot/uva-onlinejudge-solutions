from sys import stdin
from collections import defaultdict, deque

MAX_COLORS = 51



def load_num():
    return int(stdin.readline())

def load_pair():
    return tuple(map(int, stdin.readline().split()))

def load_case():
    nbeads = load_num()
    return [load_pair() for b in range(nbeads)] 

def build_necklace(beads):
    """Construct find an euler circuit in the graph defined by the
    beads"""
    # For a graph to have a euler circuits all vertices must have
    # even degree. (Plus 0 or 2 odd vertices) Init and ckeck degree
    amatrix = [defaultdict(int) for _ in range(MAX_COLORS)]
    degree = defaultdict(int)
    for b in beads:
        amatrix[b[0]][b[1]] += 1
        amatrix[b[1]][b[0]] += 1
        degree[b[0]] +=1
        degree[b[1]] +=1
    
    for k, v in degree.items():
        if v%2 != 0:
            return None

    # Create necklace using Fleury's algorithm
    def get_next_bead(color):
        """ """
        s_color, s_degree = 0, 0
        for col, deg in amatrix[color].items():
            if deg > s_degree:
                s_color, s_degree = col, deg
         
        if s_degree>0:
            amatrix[color][s_color] -= 1
            amatrix[s_color][color] -= 1
            # Removing not reachable colors should be a little faster
            if amatrix[color][s_color] == 0:
                del amatrix[color][s_color]
            if amatrix[s_color][color] == 0:
                del amatrix[s_color][color]
            return (color, s_color)
        else:
            return None

    # Initialize necklace
    nxt = get_next_bead(beads[0][1])
    necklace = deque([nxt])

    while True:
        nxt = get_next_bead(necklace[-1][1])
        if nxt:
            necklace.append(nxt)
        elif len(beads) != len(necklace):
            # Created a closed cycle.move last segment to the start
            prev = necklace.pop()
            necklace.appendleft(prev)
        else:
            break

    return necklace


if __name__ == '__main__':
    ncases = load_num()
    
    for c in range(ncases):
        beads = load_case()
        necklace = build_necklace(beads)
         
        # Print result
        print("Case #{}".format(c+1))
        if necklace:
            # Print all necklace beads together for faster IO (damn timelimits)
            # Almost a third of the time is wasted in IO
            necklace_str = ""
            for b in necklace:
                necklace_str += "{} {}\n".format(b[0], b[1])
        else:
            necklace_str = "some beads may be lost\n"

        if c+1 == ncases:
            print(necklace_str[:-1])
        else:
            print(necklace_str)
