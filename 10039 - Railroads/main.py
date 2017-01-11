import sys
from collections import defaultdict, namedtuple
from operator import itemgetter
from heapq import heappop, heappush
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

Connection = namedtuple("Connection", ['departure', 'arrival', 't_departure', 't_arrival', 'uid'])

def con_start_id(con):
    """id used for connection departure node after time expansion"""
    return con.uid*2
    
def con_end_id(con):
    """id used for connection arrival node after time expansion"""
    return con.uid*2+1


ARRIVAL = "arrival"
DEPARTURE = "departure"



#
# IO and helper functions
#
################################3


def time_to_min(time):
    """Convert time in this format hhmm into minutes passed sind 0000
    0830->510
    1345->825
    """
    minutes = time%100
    hours = time//100
    return hours*60+minutes

def time_to_str(time):
    """Convert time into 4 char string"""
    time_str = str(time)
    return "0"*(4-len(time_str))+time_str

def min_to_time(mins):
    """Convert from minutes to time, opposite to time_to_min"""
    assert mins < 1441
    minutes = mins%60
    hours = mins//60
    return hours*100+minutes

def read_num():
    return int(sys.stdin.readline())

def read_train(cities):
    nstops = read_num()
    stops = []
    assert nstops > 1
    for s in range(nstops):
        time, city = sys.stdin.readline().rstrip().split()
        stops.append((cities[city], time_to_min(int(time))))

    return stops

def read_scenario():
    """Load one scenario form stdin"""
    ncities = read_num()

    cities = [sys.stdin.readline().strip() for _ in range(ncities)]
    rcities = {citie: i for i, citie in enumerate(cities)}

    # Number of trains
    ntrains = read_num()
    trains = [read_train(rcities) for t in range(ntrains)]

    # Starting time, start city, destination city
    start = time_to_min(read_num())
    src = rcities[sys.stdin.readline().strip()]
    dst = rcities[sys.stdin.readline().strip()]

    return cities, trains, src, dst, start

def print_schedule(schedule):
    """Print schedule using accepted format into stdin"""
    if not schedule:
        print("No connection")
    else:
        src = schedule[0]
        dst = schedule[-1]
        src_time = time_to_str(min_to_time(src.t_departure))
        dst_time = time_to_str(min_to_time(dst.t_arrival))
        src_name = cities[src.departure]
        dst_name = cities[dst.arrival]
        print("Departure {} {}".format(src_time, src_name))
        print("Arrival   {} {}".format(dst_time, dst_name))
 


class PriorityQueue(object):
    """Priority queue implementation used by dijkstra algorithm from:
        https://docs.python.org/3.4/library/heapq.html
    """
    def __init__(self):
        self._heap = []
        self._entry_finder = {}
        self.REMOVED = '<removed element>'
        self.count = 0

    def add_task(self, task, priority=0):
        if task in self._entry_finder:
            self.rem_task(task)
        entry = [priority, self.count, task]
        self._entry_finder[task] = entry
        heappush(self._heap, entry)
        self.count += 1

    def rem_task(self, task):
        entry = self._entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self._heap:
            priority, count, task = heappop(self._heap)
            if task is not self.REMOVED:
                del self._entry_finder[task]
                return task

        raise KeyError('pop from an empty priority queue')

    def __contains__(self, item):
        return item in self._entry_finder

    def __len__(self):
        return len(self._heap)
#
# Solution
#
###########


def build_connection_table(cities, trains, start_time=0):
    """
    cities (dict):
    trains (list):
    start_time (int): All connections departing or arriving later than
        this will be ignored.
    """
    # Per city
    cuid = 0 # Connection unique id
    
    # List of connections ordered by id 
    connections = [] 

    # Dictionary of connections by city separated by arrival/departure
    cities = defaultdict(list)

    for schedule in trains:
        prev_city, prev_time = schedule[0]
        for city, time in schedule[1:]:
            if prev_time >= start_time:
                con = Connection(prev_city, city, prev_time, time, cuid)
                cities[(city, ARRIVAL)].append(con)
                cities[(prev_city, DEPARTURE)].append(con)
                connections.append(con)
                cuid += 1
            prev_city, prev_time = city, time

    return connections, cities


def build_time_exp_adj(cities, city_connections, connections):
    """Build time expanded adjacency list"""
    adjList = [list() for _ in range(2*len(connections))]

    # Add intercity connections (departure-arrival)
    for c in connections:
        adjList[con_start_id(c)].append((con_end_id(c), c.t_arrival-c.t_departure, c))

    # Add intracity connections, delays inside city waiting until some train departure
    for city in range(len(cities)):
        times = []

        # Append arrivals first so they are sorted first when the time
        # is the same as one departure.
        for c in city_connections[city, ARRIVAL]:
            times.append((c.t_arrival, con_end_id(c), c))
        for c in city_connections[city, DEPARTURE]:
            times.append((c.t_departure, con_start_id(c), c))

        if len(times) < 2:
            continue

        times = sorted(times, key=itemgetter(0))
       
        for node, next_node in zip(times, times[1:]):
            adjList[node[1]].append((next_node[1], next_node[0]-node[0], None))

    node_connection = {(con_start_id(c), con_end_id(c)): c for c in connections}

    return adjList, node_connection


def dijkstra(adjList, start_node):
    """Dijkstra algorithm implementation"""
    nnodes = len(adjList)
    parent = [None for _ in range(nnodes)]
    cost = [999999 for _ in range(nnodes)]

    cost[start_node] = 0
    pq = PriorityQueue()
    pq.add_task(start_node, priority=0)

    while pq:
        node = pq.pop_task()

        for v, edge_cost, _ in adjList[node]:
            if cost[node]+edge_cost<cost[v]:
                parent[v] = node
                cost[v] = cost[node]+edge_cost
                if v in pq: 
                    pq.rem_task(v)
                pq.add_task(v, priority = cost[v])

    return cost, parent


def find_path(parent, node, node_table):
    """Given the parent list returned by dijkstra, and node_table reconstruct
    conection schedule for a given node"""
    path = []
    node_p = node

    while node_p is not None:
        connection = node_table.get((parent[node_p], node_p), None)
        if connection:
            path.append(connection)

        node_p = parent[node_p]
  
    return list(reversed(path))


def find_schedule(cities, trains, src, dst, start_time):
    """Create time-expanded graph from train timetables, and then find
    shortest path from src city with Dijkstra's algorithm""" 
    # Build train connection list and dictionary containing arriving and departing
    # connections for each city
    connections, city_connections = build_connection_table(cities, trains, start_time)
    if not connections:
        return None

    # Build expanded time adjacency list
    exp_adj_list, node_table = build_time_exp_adj(cities, city_connections, connections)
 
    # Find start node for expanded graph
    start_con = city_connections[src, DEPARTURE]
    if not start_con:
        return None
    start_nodes = list(map(con_start_id, start_con))
    start_nodes = list(zip(start_nodes, start_con))

    # Add extra node to the graph representing destination city, 
    # reachable from all destination arrival nodes.
    # TODO: Add this node for each city in the graph???
    dest_con = city_connections[dst, ARRIVAL]
    if not dest_con:
        return None
    dest_nodes = list(map(con_end_id, dest_con))
    dest_node = len(exp_adj_list)
    exp_adj_list.append(list())
    for d in dest_nodes:
        exp_adj_list[d].append((dest_node, 0, None))

    # Use Dijkstra to find shortest path
    paths = []
    for s, con in start_nodes:
        time, parent = dijkstra(exp_adj_list, s)
   
        # Check there is a route to destination node
        if time[dst] > 9999:
            continue
       
        src_node = con
        dst_node = node_table[(parent[parent[dest_node]], parent[dest_node])]
        paths.append((src_node, dst_node)) 

    if not paths:
        return None

    return max(paths, key = lambda p: p[0].t_departure)


if __name__ == '__main__':

    nscenarios = read_num()
 
    for s in range(nscenarios):
        cities, trains, start_city, dst_city, start_time = read_scenario()
        schedule = find_schedule(cities, trains, start_city, dst_city, start_time)
        print("Scenario {}".format(s+1))
        print_schedule(schedule) 
        if s+1 < nscenarios:
            print('')
