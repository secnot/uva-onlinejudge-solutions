import sys
from collections import namedtuple, defaultdict

Cube = namedtuple('Cube', ['front', 'back', 'left', 'right', 'top', 'bottom', 'weight'])

class CubeRot(object):
    def __init__(self, top, bottom, weight, desc, parent=None, height=1):
        self.top = top
        self.bottom = bottom
        self.weight = weight
        self.desc = desc
        self.parent = parent
        self.height = height

def load_num():
    num_str = ''
    while num_str == '\n' or num_str=='':
        num_str = sys.stdin.readline()

    return list(map(int, num_str.rstrip().split()))


def load_next_test(): 
    cube_num = load_num()[0]
    if not cube_num:
        return None
    else:
        return [Cube(*load_num(), weight=w+1) for w in range(cube_num)]

def cube_rotations(c):

    rot = set([])
    rot.add(CubeRot(c.top, c.bottom, c.weight, 'top'))
    rot.add(CubeRot(c.bottom, c.top, c.weight, 'bottom'))
    rot.add(CubeRot(c.left, c.right, c.weight, 'left'))
    rot.add(CubeRot(c.right, c.left, c.weight, 'right'))
    rot.add(CubeRot(c.front, c.back, c.weight, 'front'))
    rot.add(CubeRot(c.back, c.front, c.weight, 'back'))

    return rot


def tallest_tower(cubes):
    """Cubes are a DAG, short in topological order and find longest path, 
    each of the 6 possible cube positions are represented as a different object
    with the same weight.
    """
   
    # Store cubes organized by top color for to accelerate searches
    by_color = defaultdict(list)
    g = []

    def add_rot_cube(r):
        for c in by_color[r.top]:
            if c.height>= r.height and c.weight<r.weight:
                r.height = c.height+1
                r.parent = c
        by_color[r.bottom].append(r)
        g.append(r)

    for new_cube in cubes:
        for rot_cube in cube_rotations(new_cube):
            add_rot_cube(rot_cube)

    # Find tower bottom 
    tower_botton = max(g, key=lambda c: c.height)
    tower = [tower_botton]

    while True:
        if not tower[-1].parent:
            break
        tower.append(tower[-1].parent)

    # Build tower in correct order
    return tower


if __name__ == '__main__':

    for i in range(1000000):
        cubes = load_next_test()
        if not cubes:
            break
        tower = tallest_tower(cubes) 

        print("Case #{}".format(i+1))
        print("{}".format(tower[0].height))
        for cube in tower[::-1]:
            print("{} {}".format(cube.weight, cube.desc))
        print('')        

    exit(0)
