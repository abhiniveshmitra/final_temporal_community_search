# Find shortest path with community jumps
def find_shortest_path_with_community_jumps(G, source, target, bridge_nodes, timestamp, communities):
    def heuristic(node):
        return 0

    def get_edge_weight(u, v):
        return G[u][v].get('base_weight', 1)

    def dijkstra_with_community_jumps(start, end, visited):
        queue = [(0, start, [])]
        while queue:
            cost, node, path = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    edge_weight = get_edge_weight(node, neighbor)
                    heapq.heappush(queue, (cost + edge_weight, neighbor, path))
        return float('inf'), []

    # Compute shortest path within each community
    intra_community_paths = {}
    for community in set(communities.values()):
        nodes_in_community = [node for node in G.nodes if communities[node] == community]
        for node in nodes_in_community:
            for target_node in nodes_in_community:
                if node != target_node:
                    cost, path = dijkstra_with_community_jumps(node, target_node, set())
                    intra_community_paths[(node, target_node)] = (cost, path)

    # Compute shortest paths using bridge nodes
    best_cost = float('inf')
    best_path = []

    for bridge_node in bridge_nodes:
        if communities[source] != communities[bridge_node] and communities[target] != communities[bridge_node]:
            cost1, path1 = dijkstra_with_community_jumps(source, bridge_node, set())
            cost2, path2 = dijkstra_with_community_jumps(bridge_node, target, set())
            total_cost = cost1 + cost2
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path1 + path2[1:]

    return best_cost, best_path
