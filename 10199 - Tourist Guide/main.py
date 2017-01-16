import sys
from itertools import count
from collections import defaultdict, deque
import enum


class VStatus(enum.IntEnum):
    Undiscovered = 0
    Discovered = 1,
    Processed = 2


class Graph(object):

    def __init__(self, edges=None, directed=False):
        self._adj = defaultdict(set)
        self._directed = directed
        if edges:
            self.add_edges(edges)
 
    def vertices(self):
        return list(self._adj.keys())

    def edges(self):
        if self._directed:
            return [(ver, e) for ver, edg in self._adj.items() for e in edg]
        else:
            edges = set()
            for ver, edg in self._adj.items():
                for e in edg:
                    edges.add((max(ver, e), min(ver, e)))
            return list(edges)

    def add_edges(self, edges):
        for v1, v2 in edges:
            self.add_edge(v1, v2)

    def add_edge(self, n1, n2):
        """Add edge between n1 and n2 (also adding vertices)"""
        self._adj[n1].add(n2)
        if not self._directed:
            self._adj[n2].add(n1)

    def del_edge(self, n1, n2):
        """ """
        self._adj[n1].remove(n2)
        if not self._directed:
            self._adj[n2].remove(n1)

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = set()

    def del_vertex(self, v):
        """Delete vertex and all edges leading to it"""
        if self._directed:
            for _, edges in self._adj.items():
                if v in edges:
                    edges.remove(v)
        else:
            for e in self._adj[v]:
                self._adj[e].remove(v)

        del self._adj[v]

    def vertex_connected(self, v1, v2):
        """is v1 directly connected to v2"""
        return v1 in self._adj and v2 in self._adj[v1]

    def is_connected(self, v=None):
        """True if graph if fully connected """
        if v is None:
            v = next(iter(self._adj.keys()))

        self._process_vertex_early = self._default_process_vertex_early
        self._process_vertex_late = self._default_process_vertex_late
        self._process_edge = self._default_process_edge
       
        self.bfs(v)

        parents = (value for key, value in self._parent.items() if key!=v)
        return all((p is not None) for p in parents)

    @staticmethod
    def _default_process_vertex_early(self, v):
        return

    @staticmethod
    def _default_process_vertex_late(self, v):
        return

    @staticmethod
    def _default_process_edge(self, v, e):
        return

    def bfs(self, start,
            process_vertex_early = None,
            process_vertex_late = None,
            process_edge = None):
        """Breath first search implementation"""
        if not process_vertex_early: 
            process_vertex_early = self._default_process_vertex_early
        if not process_vertex_late:
            process_vertex_late = self._default_process_vertex_late
        if not process_edge:
            process_edge = self._default_process_edge
        
        self._discovered = defaultdict(bool)
        self._processed = defaultdict(bool)
        self._parent = defaultdict(lambda: None)

        q = deque([start])
        self._discovered[start] = True
        while q:
            v = q.popleft()
            process_vertex_early(self, v)
            self._processed[v] = True

            for e in self._adj[v]:
                if not self._processed[e] or self._directed:
                    process_edge(self, v, e)
                if not self._discovered[e]:
                    q.append(e)
                    self._discovered[e] = True
                    self._parent[e] = v

            process_vertex_late(self, v)

    def dfs(self, v,
            process_vertex_early=None,
            process_vertex_late=None,
            process_edge=None):
        """Depth first search (recursive)"""   
        if not process_vertex_early: 
            process_vertex_early = self._default_process_vertex_early
        if not process_vertex_late:
            process_vertex_late = self._default_process_vertex_late
        if not process_edge:
            process_edge = self._default_process_edge

        self._discovered = defaultdict(bool)
        self._processed = defaultdict(bool)
        self._entry_time = defaultdict(lambda: None) # Entry time
        self._exit_time = defaultdict(lambda: None) # Exit time
        self._parent = defaultdict(lambda: None)
        self._finished = False
        self._time = count()
        
        return self._dfs(v,
                process_vertex_early,
                process_vertex_late,
                process_edge)

    def _dfs(self, v,
            process_vertex_early,
            process_vertex_late,
            process_edge):

        if self._finished:
            return

        self._discovered[v] = True
        self._entry_time[v] = next(self._time)

        process_vertex_early(self, v)

        for e in self._adj[v]:
            if not self._discovered[e]:
                self._parent[e] = v
                process_edge(self, v, e)
                self._dfs(e,
                    process_vertex_early,
                    process_vertex_late,
                    process_edge)
            elif not self._processed[e] and self._parent[v]!=e or self._directed:
                process_edge(self, v, e)

            if self._finished:
                return

        process_vertex_late(self, v)
        self._exit_time[v] = next(self._time)
        self._processed[v] = True

    def find_path(self, n1, n2):

        if len(self._adj) < 2:
            return None

        if n1 not in self._adj or n2 not in self._adj:
            raise KeyError
        self.bfs(n1)
        if self._parent[n2] is None:
            return None

        # Reconstruct path
        path = [n2]
        current = n2
        while self._parent[current] is not None:
            path.append(self._parent[current])
            current = self._parent[current]

        return list(reversed(path))

    def label_connected(self):
        """Label connected vertex of the graph with the same integer
        Returns:
            (dict): {vertex1: label, vertex2: label, ....}
        """
        assert not self._directed
        labels = {k: None for k, v in self._adj.items()}
        label = count(1)

        for v in self._adj.keys():
            if not labels[v]:
                self.bfs(v)
                next_label = next(label)
            else:
                continue

            self._parent[v] = 1 # Root node parent is allways None
            for k, v in self._parent.items():
                if self._parent[k] is not None:
                    labels[k] = next_label
 
        return labels

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._adj))

    def __repr__(self):
        return '{}({}, directed={})'.format(self.__class__.__name__, self.edges(), self._directed)



class GraphAV(Graph):
    """Graph articulation vertices"""
    
    @staticmethod
    def _av_process_vertex_early(self, v):
        self._reachable_ancestor[v] = v

    @staticmethod
    def _av_process_vertex_late(self, v):
        # Is a root node 
        if self._parent[v] is None:
            if self._tree_out_degree[v] > 1:
                self._articulation_points.add(v)
            return

        # Test if parent is root
        parent_root = self._parent[self._parent[v]] is None

        if not parent_root:
            if self._reachable_ancestor[v] == self._parent[v]:
                self._articulation_points.add(self._parent[v])
            if self._reachable_ancestor[v] == v:
                self._articulation_points.add(self._parent[v])

                # Check it is not a leaf
                if self._tree_out_degree[v] > 0:
                    self._articulation_points.add(v)

        time_v = self._entry_time[self._reachable_ancestor[v]]
        time_parent = self._entry_time[self._reachable_ancestor[self._parent[v]]]

        if time_v < time_parent:
            self._reachable_ancestor[self._parent[v]] = self._reachable_ancestor[v]

    @staticmethod
    def _av_process_edge(self, v, e):
       
        edge_class = self._av_edge_class(v, e)

        if edge_class == "tree":
            self._tree_out_degree[v] += 1

        if edge_class == "back" and self._parent[v] != e:
            if self._entry_time[e] < self._entry_time[self._reachable_ancestor[v]]:
                self._reachable_ancestor[v] = e

    def _av_edge_class(self, v, e):
        if self._parent[e] == v: return "tree"
        if self._discovered[e] and not self._processed[e]: return "back"
        if self._processed[e] and (self._entry_time[e]>self._entry_time[v]): return "forward"
        if self._processed[e] and (self._entry_time[e]<self._entry_time[v]): return "cross"

    def find_articulation(self):
        """Split graph into connected subgraphs, and then find articulation points
        with in each one."""
        if len(self._adj) < 3:
            return []

        # Label each connected subgraph
        labels = self.label_connected()


        
        av = []
        seen_labels = set()
        for v, label in labels.items():
            if label is None or label in seen_labels:
                continue

            av += self._find_articulations(v)
        
        # Discard repeated vertices
        return list(set(av))

    def _find_articulations(self, v):
        self._reachable_ancestor = defaultdict(lambda: None)
        self._tree_out_degree = defaultdict(int)
        self._articulation_points = set()
        
        self.dfs(v,
            self._av_process_vertex_early,
            self._av_process_vertex_late,
            self._av_process_edge)
        
        return list(self._articulation_points)


 

def read_num():
    return int(sys.stdin.readline())

def load_locations(nlocations):
    locations = [sys.stdin.readline().rstrip() for _ in range(nlocations)]
    return {loc:num for num, loc in enumerate(locations)}

def load_routes(nroutes, loc_table): 
    routes = [sys.stdin.readline().rstrip().split() for _ in range(nroutes)]
    return [(loc_table[start], loc_table[end]) for start, end in routes]

def load_map():
    nlocations = read_num()
    if nlocations == 0:
        return None, None
    locations = load_locations(nlocations)

    #
    routes = load_routes(read_num(), locations)    
    g = GraphAV()
    g.add_edges(routes)
    return g, {num: loc for loc, num in locations.items()}


if  __name__ == '__main__':


    results = []
    while True:
        graph, locations = load_map()
        if not graph:
            break

        art = graph.find_articulation()
        results.append([a for a in sorted(locations[a] for a in art)])


    for n, r in enumerate(results):
    
        print('City map #{}: {} camera(s) found'.format(n+1, len(r)))
        if len(r) > 0:
            [print(a) for a in r]

        if n+1<len(results):
            print('')

