# Calculate gravity  table for edges
def calculate_gravity_table(G):
    GravityTable = []
    for edge in G.edges():
        node1, node2 = edge
        weight1 = G.nodes[node1]['weight']
        weight2 = G.nodes[node2]['weight']
        base_weight = G.edges[edge].get('base_weight', 1)
        traffic_density = G.edges[edge].get('traffic_density', 1)
        distance = G.edges[edge].get('length', 1)
        community_size_penalty = 0.1
        community_size = 5
        gravity = round((weight1 * weight2 * traffic_density * base_weight) / distance - (community_size_penalty * community_size), 2)
        GravityTable.append((node1, node2, gravity))
    return GravityTable
