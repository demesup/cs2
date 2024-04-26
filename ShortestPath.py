from collections import defaultdict


def dfs(graph, start, end, path=None, weight=0):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path, weight
    path_found = None
    shortest_weight = float('inf')
    for node, edge_weight in graph[start]:
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
    for node, edge_weight in graph[start]:
        if node not in path:
            node_path, node_weight = dfs_nodes(graph, node, end, path, weight + edge_weight)
            if node_path and (node_weight < shortest_weight or (
                    node_weight == shortest_weight and len(node_path) < len(shortest))):
                shortest = node_path
                shortest_weight = node_weight
    return shortest, shortest_weight


network = defaultdict(list)
network['Broadcast'] = [('A', 0)]
network['A'] = [('B', 2), ('C', 3)]
network['B'] = [('A', 2), ('C', 1), ('D', 1), ('E', 4)]
network['C'] = [('A', 3), ('B', 1), ('F', 5), ('Listener 1', 0)]
network['D'] = [('E', 1), ('B', 1), ('Listener 2', 0)]
network['E'] = [('F', 1), ('B', 1), ('D', 1), ('Listener 3', 0)]
network['F'] = [('G', 1), ('E', 1), ('C', 5)]
network['G'] = [('Listener 4', 0)]

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
