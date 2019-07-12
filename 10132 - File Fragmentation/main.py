from sys import stdin
from collections import deque

BOTH = 'B'

def readcase():
   
    fragments = []

    while True:
        frag = stdin.readline().strip()
        if len(frag) == 0:
            break
        fragments.append(frag)

    return list(map(list, fragments))
 
def can_place_left(fragment, pattern):
    matches = 0
    for f, p in zip(fragment, pattern):
        if p==BOTH:
            continue
        elif p==f:
            matches += 1
        else:
            return -1
    return len(fragment)-matches 

def can_place_right(fragment, pattern):
    matches = 0
    for f, p in zip(reversed(fragment), reversed(pattern)):
        if p==BOTH:
            continue
        elif p==f:
            matches+=1
        else:
            return -1
    return len(fragment)-matches


def update_pattern_left(fragment, pattern):
    return fragment+pattern[len(fragment):]

def update_pattern_right(fragment, pattern):
    return pattern[:len(pattern)-len(fragment)]+fragment

def rebuild_file(fragments):

    nfiles = len(fragments)//2
    file_length = sum(len(f) for f in fragments)//nfiles

    fragments = sorted(fragments, key=len, reverse=True)
    queue = deque()
    queue.append((update_pattern_left(fragments[0], [BOTH]*file_length), 0))
    queue.append((update_pattern_right(fragments[0], [BOTH]*file_length), 0))

    # Use DFS placing fragments until there is a collision, then backtrack
    while queue:
        pattern, fragidx = queue.pop()
        fragidx += 1
            
        # If we reached the last fragment without conficts the pattern is valid
        if fragidx>=len(fragments):
            if BOTH in pattern: # Check the pattern is full
                continue
            else:
                break

        # Add last the placement that changes more undefined positions in the pattern
        # so it is poped first next loop
        placel = can_place_left(fragments[fragidx], pattern)
        placer = can_place_right(fragments[fragidx], pattern)

        if placel>=placer:
            if placer>=0:
                queue.append((update_pattern_right(fragments[fragidx], pattern), fragidx))
            if placel>=0:
                queue.append((update_pattern_left(fragments[fragidx], pattern), fragidx))
        else:
            if placel>=0:
                queue.append((update_pattern_left(fragments[fragidx], pattern), fragidx))
            if placer>=0:
                queue.append((update_pattern_right(fragments[fragidx], pattern), fragidx))

    return ''.join(pattern)

if __name__ == '__main__':
    
    ncases = int(stdin.readline())

    _ = stdin.readline()
    for c in range(ncases):
        
        fragments = readcase()

        print(rebuild_file(fragments))
        if c+1<ncases:
            print()
