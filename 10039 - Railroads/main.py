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


ARRIVAL =  10 #"arrival"
DEPARTURE = 12 # "departure"



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
        self._count = 0

    def add_task(self, task, priority=0):
        if task in self._entry_finder:
            self.rem_task(task)
        entry = [priority, self._count, task, False]
        self._entry_finder[task] = entry
        heappush(self._heap, entry)
        self._count += 1

    def rem_task(self, task):
        entry = self._entry_finder.pop(task)
        entry[-1] = True # Mark as removed
        entry[-2] = None # 

    def pop_task(self):
        while self._heap:
            priority, count, task, removed = heappop(self._heap)
            if not removed:
                del self._entry_finder[task]
                return task

        raise KeyError('pop from an empty priority queue')

    def __contains__(self, item):
        return item in self._entry_finder

    def __len__(self):
        return len(self._entry_finder)

    def __str__(self):
        return str(self._heap)
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


def build_time_exp_adj(city_connections, connections):
    """Build time expanded adjacency list"""
    adjList = [list() for _ in range(2*len(connections))]

    # Add intercity connections (departure-arrival)
    for c in connections:
        adjList[con_start_id(c)].append((con_end_id(c), c.t_arrival-c.t_departure, c))

    # Add intracity connections, delays inside city waiting until some train departure
    for city in range(len(city_connections)//2):
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
            if cost[node]+edge_cost<=cost[v]:
                parent[v] = node
                cost[v] = cost[node]+edge_cost
                if v in pq: 
                    pq.rem_task(v)
                pq.add_task(v, priority = cost[v])

    return cost, parent


def dijkstra_del(adjList, city_node, start_node):
    """Dijkstra algorithm implementation"""
    nnodes = len(adjList)
    parent = [None for _ in range(nnodes)]
    cost = [999999 for _ in range(nnodes)]
    departure = [-1 for _ in range(nnodes)]

    pq = PriorityQueue()

    # Set departure value for starting nodes:
    for v, _, _ in adjList[city_node]:
        for w, edge_cost, connection in adjList[v]:
            if connection:
                departure[v] = connection.t_departure


    # Add start node
    pq.add_task(start_node, priority = -departure[start_node])
    cost[start_node] = 0

    # 
    while pq:
        #print(pq)
        node = pq.pop_task()

        for v, edge_cost, connection in adjList[node]:
            #print(cost[node]+edge_cost, cost[v], departure[node], departure[v]) 
            if cost[node] + edge_cost < cost[v]:
                parent[v] = node
                if v in pq: 
                    pq.rem_task(v)
                if departure[v] < 0:
                    departure[v] = departure[node]
                cost[v] = cost[node]+edge_cost
                pq.add_task(v, priority = -departure[v])

            elif cost[node]+edge_cost == cost[v] and departure[node] > departure[v]:
                #print("here")
                parent[v] = node
                if v in pq: 
                    pq.rem_task(v)
                departure[v] = departure[node]
                pq.add_task(v, priority = -departure[v])


    #print(parent)
    #print(departure)
    #print(cost)
    return parent



def find_path(parent_lst, node, src_city, node_table):
    """Given the parent list returned by dijkstra, and node_table reconstruct
    conection schedule for a given node"""
    path = []
    while node is not None:
        connection = node_table.get((parent_lst[node], node), None)
        if connection:
            path.append(connection)
            if connection.departure == src_city:
                break

        node = parent_lst[node]
 
    return (path[-1], path[0])
    #return list(reversed(path))


def find_schedule(cities, trains, src_city, dst_city, start_time):
    """Create time-expanded graph from train timetables, and then find
    shortest path from src city with Dijkstra's algorithm""" 
    # Build train connection list and dictionary containing arriving and departing
    # connections for each city
    connections, city_connections = build_connection_table(cities, trains, start_time) 
    start_con = city_connections[src_city, DEPARTURE]
    dest_con = city_connections[dst_city, ARRIVAL]
    if not connections or len(start_con)==0 or len(dest_con)==0:
        return None

    # Build expanded time adjacency list
    exp_adj_list, node_table = build_time_exp_adj(city_connections, connections)
 
    # Add extra node to the graph representing destination city, 
    # reachable from all destination arrival nodes.
    dest_node = len(exp_adj_list)
    exp_adj_list.append(list())
    for d in list(map(con_end_id, dest_con)):
        exp_adj_list[d].append((dest_node, 0, None))

    # Add extra node to the graph representing source city, 
    # that links to all start nodes
    start_city_node = len(exp_adj_list)
    exp_adj_list.append([(con_start_id(c), 0, None) for c in start_con])
    
    start_node = con_start_id(min(start_con, key=lambda c: c.t_departure))

    # Find path
    parent = dijkstra_del(exp_adj_list, start_city_node, start_node)
    if parent[dest_node] == None:
        return None
        
    return find_path(parent, dest_node, src_city, node_table)


if __name__ == '__main__':

    nscenarios = read_num()
 
    for s in range(nscenarios):
        cities, trains, start_city, dst_city, start_time = read_scenario()
        if s+1 != nscenarios:
            pass #continue
        path = find_schedule(cities, trains, start_city, dst_city, start_time)
        print("Scenario {}".format(s+1))
        print_schedule(path) 
        print('')
