from sys import stdin
from collections import deque


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def readdict():
    d = set()
    while True:
        word = stdin.readline().strip()
        if len(word) == 0:
            break
        d.add(word)

    return d

def readwords():
    cases = []

    while True:
        case = tuple(stdin.readline().split())
        if not case:
            break
        cases.append(case)
    return cases

def word_mods(w, dictionary):
    """Return list of all valid step modifications from a given word"""
    mods = []

    for pos in range(len(w)):
        for c in ALPHABET: 
            word = w[:pos]+c+w[(pos+1):]
            if word in dictionary and word!=w:
                mods.append(word)  

    return mods


def find_solution(start, end, dictionary):
    """Use BFS to find shortest path from start to end words"""
    if start == end:
        return [start, end]

    # Add endword to dictionary
    add_end = end not in dictionary
    if add_end:
        dictionary.add(end)

    # BFS Search
    parent = {}
    q = deque([start])
   
    while q:
        word = q.popleft()

        if word == end:
            break

        # Enqueue word mods that haven't been reached yet.
        for w in word_mods(word, dictionary):
            if w not in parent:
                parent[w] = word
                q.append(w) 

    # Restore dictionary to original state
    if add_end:
        dictionary.remove(end)

    if word != end:
        return []
    
    # Reconstruct modification path
    path = [word]
    while parent[word]!= start:
        path.append(parent[word])
        word = parent[word]
    path.append(start)

    return list(reversed(path))
    

if __name__ == '__main__':

    dictionary = readdict()
    words = list(reversed(readwords()))

    while words:
        start, end = words.pop()
        
        sequence = find_solution(start, end, dictionary)
        if not sequence:
            print('No solution.')
        else:
            [print(w) for w in sequence]

        if words:
            print()
