# Main function to integrate all calculations
def main():
    num_nodes = 100
    num_edges = 500
    G = generate_synthetic_graph(num_nodes, num_edges)

    # Find optimal threshold for community assignment
    num_communities_desired_range = (20, 25)
    threshold = find_optimal_threshold(G, num_communities_desired_range)

    if threshold is None:
        print("Failed to find a suitable threshold.")
        return

    # Assign nodes to communities
    communities = assign_nodes_to_communities(G, threshold)
    
    # Find community bridges
    bridge_nodes = find_community_bridges(G, communities)

    # Randomly select source, target, and timestamp
    source = random.choice(list(G.nodes))
    target = random.choice(list(G.nodes))
    while source == target:  # Ensure source and target are different
        target = random.choice(list(G.nodes))
    timestamp = random.randint(0, 23)  # Adjust range as needed

    # Find shortest path with community jumps
    cost, path = find_shortest_path_with_community_jumps(G, source, target, bridge_nodes, timestamp, communities)
    print(f"Source: {source}, Target: {target}, Timestamp: {timestamp}")
    print(f"Shortest path cost from {source} to {target}: {cost:.2f}")
    print(f"Shortest path: {path}")

    # Plot the graph with the path highlighted
    plot_graph(G, communities, path)

if __name__ == "__main__":
    main()
