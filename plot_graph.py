# Plot the graph
def plot_graph(G, communities, path=None):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))

    # Draw nodes
    community_colors = list(communities.values())
    nx.draw_networkx_nodes(G, pos, node_size=100, cmap=plt.cm.viridis, node_color=community_colors)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    
    if path:
        # Draw edges in the path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.5)
    
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    plt.title("Graph with Node Communities and Path Highlighted")
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), label='Community')
    plt.show()
