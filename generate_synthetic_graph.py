# Generate synthetic graph with weighted edges
def generate_synthetic_graph(num_nodes, num_edges):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i, weight=round(random.uniform(0.5, 2.0), 2))
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and not G.has_edge(u, v):
            node_u_weight = G.nodes[u]['weight']
            node_v_weight = G.nodes[v]['weight']
            base_weight = round(node_u_weight * node_v_weight, 2)
            G.add_edge(u, v, base_weight=base_weight, length=round(random.uniform(1, 10), 2), traffic_density=round(random.uniform(0.5, 1.5), 2))
    return G
