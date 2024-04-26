from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))

    def get_neighbors(self, node):
        return self.graph[node]

    def get_all_nodes(self):
        return self.graph.keys()


def dfs(graph, start, end, path=None, weight=0):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path, weight
    path_found = None
    shortest_weight = float('inf')
    for node, edge_weight in graph.get_neighbors(start):
        if node not in path:
            new_path, new_weight = dfs(graph, node, end, path, weight + edge_weight)
            if new_path and new_weight < shortest_weight:
                path_found = new_path
                shortest_weight = new_weight
    if path_found is not None:
        return path_found, shortest_weight
    else:
        return None, float('inf')


def dfs_nodes(graph, start, end, path=None, weight=0):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path, weight
    shortest = None
    shortest_weight = float('inf')
    for node, edge_weight in graph.get_neighbors(start):
        if node not in path:
            node_path, node_weight = dfs_nodes(graph, node, end, path, weight + edge_weight)
            if node_path and (node_weight < shortest_weight or (
                    node_weight == shortest_weight and len(node_path) < len(shortest))):
                shortest = node_path
                shortest_weight = node_weight
    return shortest, shortest_weight


network = Graph()
network.add_edge('Broadcast', 'A', 0)
network.add_edge('A', 'B', 2)
network.add_edge('A', 'C', 3)
network.add_edge('B', 'A', 2)
network.add_edge('B', 'C', 1)
network.add_edge('B', 'D', 1)
network.add_edge('B', 'E', 4)
network.add_edge('C', 'A', 3)
network.add_edge('C', 'B', 1)
network.add_edge('C', 'F', 5)
network.add_edge('C', 'Listener 1', 0)
network.add_edge('D', 'E', 1)
network.add_edge('D', 'B', 1)
network.add_edge('D', 'Listener 2', 0)
network.add_edge('E', 'F', 1)
network.add_edge('E', 'B', 1)
network.add_edge('E', 'D', 1)
network.add_edge('E', 'Listener 3', 0)
network.add_edge('F', 'G', 1)
network.add_edge('F', 'E', 1)
network.add_edge('F', 'C', 5)
network.add_edge('G', 'Listener 4', 0)

start_node = 'Broadcast'
listeners = ['Listener 1', 'Listener 2', 'Listener 3', 'Listener 4']

for listener in listeners:
    print('\n')
    shortest_path, total_weight = dfs(network, start_node, listener)
    if shortest_path:
        print(f"Shortest path to {listener}:", shortest_path)
        print(f"Total weight to {listener}:", total_weight)
    else:
        print(f"No path found to {listener}.")

    shortest_path_to_listener_with_skip, total_weight_to_listener_with_skip = dfs_nodes(network, start_node, listener)
    if shortest_path_to_listener_with_skip:
        print(f"Shortest path to {listener} (with nodes):", shortest_path_to_listener_with_skip)
        print(f"Total weight to {listener} (with nodes):", total_weight_to_listener_with_skip)
    else:
        print(f"No path found to {listener}.")
