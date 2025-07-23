# Import necessary libraries
import networkx as nx
import random
import heapq
import matplotlib.pyplot as plt
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------------
# A* Algorithm Implementation
# -------------------------------

def a_star_search(G, start, goal, heuristic=None):
    """
    A* algorithm for finding the shortest path between start and goal in graph G.
    If no heuristic is provided, it defaults to Dijkstra's algorithm.

    Parameters:
    - G: NetworkX graph
    - start: Starting node
    - goal: Target node
    - heuristic: A function that estimates the cost from a node to the goal

    Returns:
    - Tuple (total_cost, path)
      - total_cost: Total cost of the path
      - path: List of nodes representing the path
    """
    if heuristic is None:
        heuristic = lambda x: 0  # No heuristic, behaves like Dijkstra's

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start), start))
    came_from = {}
    g_score = {node: float('inf') for node in G.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in G.nodes}
    f_score[start] = heuristic(start)

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return g_score[goal], path[::-1]

        for neighbor in G.neighbors(current):
            edge_data = G.get_edge_data(current, neighbor, default={})
            weight = edge_data.get('base_weight', 1)  # Default weight is 1 if not specified
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                # Add neighbor to open_set if not already present
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return float('inf'), []  # No path found

# -------------------------------
# Community Detection Functions
# -------------------------------

def assign_nodes_to_communities_fixed_size(G, community_size=25):
    """
    Assigns nodes to communities with approximately 'community_size' nodes each.
    Uses a gravity-based approach to ensure connectivity within communities.

    Parameters:
    - G: NetworkX graph
    - community_size: Desired number of nodes per community

    Returns:
    - Dictionary mapping each node to its community number
    """
    def calculate_gravitational_force(node1, node2):
        """
        Calculates the gravitational force between two nodes based on their weights and edge attributes.
        """
        weight1 = G.nodes[node1]['weight']
        weight2 = G.nodes[node2]['weight']
        base_weight = G.edges[node1, node2].get('base_weight', 1)
        traffic_density = G.edges[node1, node2].get('traffic_density', 1)
        length = G.edges[node1, node2].get('length', 1)
        gravity = (weight1 * weight2 * traffic_density * base_weight) / length
        return gravity

    unassigned_nodes = set(G.nodes())
    communities = {}
    community_number = 1

    while unassigned_nodes:
        # Select a random unassigned node as the seed
        seed = random.choice(list(unassigned_nodes))
        queue = [seed]
        communities[seed] = community_number
        unassigned_nodes.remove(seed)
        current_size = 1

        while queue and current_size < community_size:
            current = queue.pop(0)
            neighbors = list(G.neighbors(current))
            # Calculate gravitational force for each neighbor and sort by descending force
            neighbors.sort(key=lambda neighbor: calculate_gravitational_force(current, neighbor), reverse=True)

            for neighbor in neighbors:
                if neighbor in unassigned_nodes:
                    communities[neighbor] = community_number
                    unassigned_nodes.remove(neighbor)
                    queue.append(neighbor)
                    current_size += 1
                    if current_size >= community_size:
                        break

        community_number += 1

    return communities

def find_community_bridges(G, communities):
    """
    Identifies bridge edges that connect different communities.

    Parameters:
    - G: NetworkX graph
    - communities: Dictionary mapping nodes to communities

    Returns:
    - Set of tuples representing bridge edges (node, neighbor)
    """
    bridge_edges = set()
    for u, v in G.edges():
        if communities[u] != communities[v]:
            bridge_edges.add((u, v))
    return bridge_edges

# -------------------------------
# Graph Remodeling Function
# -------------------------------

def create_community_graph(G, communities, bridges):
    """
    Creates a remodeled graph where each community is treated as a single node.
    Edges between communities represent bridge connections.

    Parameters:
    - G: Original NetworkX graph
    - communities: Dictionary mapping nodes to communities
    - bridges: Set of bridge edges (node, neighbor)

    Returns:
    - Remodeled NetworkX graph
    """
    community_graph = nx.Graph()
    community_ids = set(communities.values())
    
    # Add community nodes
    for cid in community_ids:
        community_graph.add_node(cid)
    
    # Add edges between communities based on bridges
    for bridge in bridges:
        u, v = bridge
        community_u = communities[u]
        community_v = communities[v]
        if community_u != community_v:
            weight = G[u][v]['base_weight']
            if community_graph.has_edge(community_u, community_v):
                # If multiple bridges exist, keep the one with the minimum weight
                current_weight = community_graph[community_u][community_v]['base_weight']
                community_graph[community_u][community_v]['base_weight'] = min(current_weight, weight)
            else:
                community_graph.add_edge(community_u, community_v, base_weight=weight)
    return community_graph

# -------------------------------
# Synthetic Graph Generation
# -------------------------------

def generate_synthetic_graph(num_nodes, num_edges):
    """
    Generates a synthetic graph with specified number of nodes and edges.
    Nodes have random weights, and edges have attributes like base_weight, length, and traffic_density.

    Parameters:
    - num_nodes: Number of nodes
    - num_edges: Number of edges

    Returns:
    - NetworkX graph
    """
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i, weight=round(random.uniform(0.5, 2.0), 2))
    edge_count = 0
    while edge_count < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and not G.has_edge(u, v):
            node_u_weight = G.nodes[u]['weight']
            node_v_weight = G.nodes[v]['weight']
            base_weight = round(node_u_weight * node_v_weight, 2)
            length = round(random.uniform(1, 10), 2)
            traffic_density = round(random.uniform(0.5, 1.5), 2)
            G.add_edge(u, v, base_weight=base_weight, length=length, traffic_density=traffic_density)
            edge_count += 1
    return G

# -------------------------------
# Visualization Function
# -------------------------------

def plot_graph(G, communities, path=None):
    """
    Plots the graph with communities colored differently and optionally highlights a path.

    Parameters:
    - G: NetworkX graph
    - communities: Dictionary mapping nodes to communities
    - path: List of nodes representing the path to highlight
    """
    pos = nx.spring_layout(G, seed=42)  # For consistent layout
    plt.figure(figsize=(12, 8))

    # Assign a unique color to each community
    unique_communities = list(set(communities.values()))
    color_map = {cid: idx for idx, cid in enumerate(unique_communities)}
    community_colors = [color_map[communities[node]] for node in G.nodes]

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=100, cmap=plt.cm.viridis, node_color=community_colors)
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.5)

    # Highlight path if provided
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.5)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

    plt.title("Graph with Node Communities and Path Highlighted")
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), label='Community')
    plt.axis('off')
    plt.show()

# -------------------------------
# Main Execution Function
# -------------------------------

def main():
    # Parameters
    num_nodes = 1000
    num_edges = 3500
    train_queries = 500
    test_queries = 500
    desired_community_size = 25  # Aim for 20-25 nodes per community

    # Step 1: Generate Synthetic Graph
    print("Generating synthetic graph...")
    G = generate_synthetic_graph(num_nodes, num_edges)
    print(f"Graph generated with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.\n")

    # Step 2: Assign Nodes to Fixed-Size Communities
    print("Assigning nodes to communities with approximately 20-25 nodes each...")
    communities = assign_nodes_to_communities_fixed_size(G, community_size=desired_community_size)
    num_communities = len(set(communities.values()))
    print(f"Total communities formed: {num_communities}\n")

    # Step 3: Identify Bridge Nodes
    print("Identifying bridge edges between communities...")
    bridges = find_community_bridges(G, communities)
    print(f"Total bridge edges identified: {len(bridges)}\n")

    # Step 4: Remodel the Graph Based on Communities
    print("Creating remodeled community graph...")
    community_graph = create_community_graph(G, communities, bridges)
    print(f"Remodeled community graph has {community_graph.number_of_nodes()} nodes and {community_graph.number_of_edges()} edges.\n")

    # -------------------------------
    # Train/Test Process
    # -------------------------------

    # Step 5: Run Training Queries to Calculate Average Distance Loss
    print(f"Running {train_queries} training queries to calculate average distance loss...\n")
    training_distance_diffs = []
    original_times_train = []
    remodeled_times_train = []

    def training_query(query_id, start, goal):
        # A* on Original Graph
        start_time = time.time()
        original_cost, _ = a_star_search(G, start, goal)
        original_time = time.time() - start_time

        # A* on Remodeled Community Graph
        start_time = time.time()
        remodeled_cost, _ = a_star_search(community_graph, communities[start], communities[goal])
        remodeled_time = time.time() - start_time

        # Calculate Distance Difference
        if original_cost != float('inf') and remodeled_cost != float('inf'):
            distance_diff = original_cost - remodeled_cost
            training_distance_diffs.append(distance_diff)
        else:
            # Handle cases where no path exists
            training_distance_diffs.append(0)  # Assuming no loss if no path exists

        # Record execution times
        original_times_train.append(original_time)
        remodeled_times_train.append(remodeled_time)

    # Generate all training queries upfront
    training_queries = [(random.choice(list(G.nodes)), random.choice(list(G.nodes))) for _ in range(train_queries)]

    # Execute training queries in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(training_query, i, q[0], q[1]) for i, q in enumerate(training_queries)]
        for _ in as_completed(futures):
            pass  # No action needed, just wait for all to complete

    # Compute Average Distance Difference from Training Set
    avg_distance_diff_training = sum(training_distance_diffs) / len(training_distance_diffs)
    print(f"Average distance difference from training set: {avg_distance_diff_training:.2f}\n")

    # Step 6: Run Testing Queries and Adjust Remodeled Distances
    print(f"Running {test_queries} testing queries and adjusting remodeled distances...\n")
    testing_distance_diffs = []
    original_times_test = []
    remodeled_times_test = []

    def testing_query(query_id, start, goal):
        # A* on Original Graph
        start_time = time.time()
        original_cost, _ = a_star_search(G, start, goal)
        original_time = time.time() - start_time

        # A* on Remodeled Community Graph
        start_time = time.time()
        remodeled_cost, _ = a_star_search(community_graph, communities[start], communities[goal])
        remodeled_time = time.time() - start_time

        # Adjust Remodeled Distance by Adding Average Training Distance Difference
        if remodeled_cost != float('inf'):
            adjusted_remodeled_cost = remodeled_cost + avg_distance_diff_training
        else:
            adjusted_remodeled_cost = float('inf')

        # Calculate Adjusted Distance Difference
        if original_cost != float('inf') and adjusted_remodeled_cost != float('inf'):
            distance_diff = adjusted_remodeled_cost - original_cost
            testing_distance_diffs.append(distance_diff)
        else:
            # Handle cases where no path exists
            testing_distance_diffs.append(0)  # Assuming no loss if no path exists

        # Record execution times
        original_times_test.append(original_time)
        remodeled_times_test.append(remodeled_time)

    # Generate all testing queries upfront
    testing_queries = [(random.choice(list(G.nodes)), random.choice(list(G.nodes))) for _ in range(test_queries)]

    # Execute testing queries in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(testing_query, i, q[0], q[1]) for i, q in enumerate(testing_queries)]
        for _ in as_completed(futures):
            pass  # No action needed, just wait for all to complete

    # -------------------------------
    # Calculate and Display Performance Metrics
    # -------------------------------

    print("\n--- Performance Comparison (Testing Set) ---\n")

    # Total Execution Times
    total_time_original_test = sum(original_times_test)
    total_time_remodeled_test = sum(remodeled_times_test)
    total_time_diff_test = total_time_original_test - total_time_remodeled_test  # Positive if time was saved

    # Total Distance Differences
    total_distance_diff_test = sum(testing_distance_diffs)

    # Percentage Calculations
    percent_time_saved = (total_time_diff_test / total_time_original_test) * 100 if total_time_original_test != 0 else 0
    total_distance_original_test = sum(training_distance_diffs[:test_queries])  # Approximation
    percent_distance_loss = (total_distance_diff_test / total_distance_original_test) * 100 if total_distance_original_test != 0 else 0

    print(f"Total A* time on original graph (Testing): {total_time_original_test:.4f} seconds")
    print(f"Total A* time on remodeled graph (Testing): {total_time_remodeled_test:.4f} seconds")
    print(f"Total time saved: {total_time_diff_test:.4f} seconds ({percent_time_saved:.2f}%)\n")

    print(f"Total distance difference (Testing): {total_distance_diff_test:.2f}")
    print(f"Percentage of distance loss: {percent_distance_loss:.2f}%\n")

    # -------------------------------
    # Visualization of Performance Metrics
    # -------------------------------

    # Plot Execution Time Comparison
    plt.figure(figsize=(12, 6))
    plt.hist(original_times_test, bins=30, alpha=0.5, label='Original Graph')
    plt.hist(remodeled_times_test, bins=30, alpha=0.5, label='Remodeled Graph')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.title('A* Execution Time on Original vs Remodeled Graph (Testing Set)')
    plt.show()

    # Plot Distance Difference
    plt.figure(figsize=(12, 6))
    plt.hist(testing_distance_diffs, bins=30, color='g', alpha=0.7)
    plt.xlabel('Adjusted Distance Difference')
    plt.ylabel('Frequency')
    plt.title('Adjusted Distance Difference between Original and Remodeled Graphs (Testing Set)')
    plt.show()

    # -------------------------------
    # Visualization of an Example Path
    # -------------------------------

    example_source, example_target = random.choice(testing_queries)
    example_cost, example_path = a_star_search(G, example_source, example_target)
    print(f"Example shortest path from {example_source} to {example_target}: {example_path} with cost {example_cost}")
    plot_graph(G, communities, example_path)

# -------------------------------
# Execute Main Function
# -------------------------------

if __name__ == "__main__":
    main()
