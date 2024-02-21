from collections import Counter, defaultdict, OrderedDict
from collections import namedtuple, deque, ChainMap, UserDict, UserList, UserString

class Graph:
    def __init__(self):
        self.nodes = set()  # To store nodes
        self.edges = dict()  # To store edges with weights
        self.distances = dict()  # To store distances

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_directional_edge(from_node, to_node, distance)
        self._add_directional_edge(to_node, from_node, distance)  # This line makes it undirected

    def _add_directional_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges.get(min_node, []):
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

# Example usage
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 5)
graph.add_edge("B", "D", 10)
graph.add_edge("C", "D", 3)
graph.add_edge("D", "E", 4)
graph.add_edge("E", "F", 2)

visited, path = dijkstra(graph, 'A')  # Find shortest path from node 'A' to all other nodes
print("Visited:", visited)
print("Path:", path)
