# Find community bridges
def find_community_bridges(G, communities):
    bridge_nodes = set()
    community_pairs = [(c1, c2) for c1 in set(communities.values()) for c2 in set(communities.values()) if c1 < c2]
    for community1, community2 in community_pairs:
        for node in G.nodes:
            if communities[node] == community1 or communities[node] == community2:
                neighbors = list(G.neighbors(node))
                for neighbor in neighbors:
                    if communities[neighbor] != communities[node]:
                        bridge_nodes.add(node)
                        break
    return bridge_nodes
