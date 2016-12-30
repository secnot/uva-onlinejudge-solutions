import sys
from collections import deque
from math import ceil



def load_num(ignore_empty_lines=True):

    num_str = sys.stdin.readline()

    if num_str == '\n' or num_str=='':
        if ignore_empty_lines:
            return load_num(ignore_empty_lines)
        else:    
            return None

    return list(map(int, num_str.rstrip().split()))


def load_scenario():
    cities, roads = load_num()
    if cities == roads == 0:
        return None

    adjList = [list() for x in range(cities+1)]
    for r in range(roads):
        c1, c2, p = load_num()
        adjList[c1].append((c2, p))
        adjList[c2].append((c1, p))
    start, destination, tourists = load_num()


    return adjList, start, destination, tourists
   

def best_route_max_passengers(adjList, start, dest):
    """Find route with most passengers per trip using BFS, and return
    its max passengers per trip""" 
    vertices = len(adjList)
    discovered = [False for v in range(vertices)]
    processed = [False for v in range(vertices)]
    parent = [-1 for v in range(vertices)]
    passengers = [-1 for v in range(vertices)]

    q = deque([start])
    discovered[start] = True
    passengers[start] = 1000000000
    
    while q:
        v = q.popleft()
        processed[v]=True

        for n in adjList[v]:
            c, p = n # city, max_passangers
        
            if not discovered[c]:
                passengers[c] = min(p, passengers[v])
                discovered[c] = True
                parent[c] = v
                q.append(c)
            elif passengers[c]<min(p,passengers[v]):
                parent[c] = v
                passengers[c] = min(p,passengers[v])
                if processed[c]:
                    processed[c] = False
                    q.append(c)


    return passengers[dest]



if __name__ == '__main__':

    for s in range(1, 200):
        scenario = load_scenario()
        if not scenario:
            break

        adjList, start, dest, passengers = scenario
        passengers_trip = best_route_max_passengers(adjList, start, dest)
        trips = ceil((passengers)/(passengers_trip-1)) # Remember the guide
        print("Scenario #{}".format(s))
        print("Minimum Number of Trips = {}\n".format(trips))
    
    exit(0)
