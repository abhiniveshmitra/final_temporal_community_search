# Find optimal threshold for community assignment
def find_optimal_threshold(G, num_communities_desired_range, max_iterations=1000):
    low = 0
    high = 15
    iteration = 0
    while iteration < max_iterations:
        threshold = (low + high) / 2
        CommunityTable = assign_nodes_to_communities(G, threshold)
        if not CommunityTable:
            print("CommunityTable is empty. Adjusting threshold.")
            low = threshold
            iteration += 1
            continue
        num_communities = len(set(CommunityTable.values()))
        if num_communities_desired_range[0] <= num_communities <= num_communities_desired_range[1]:
            return threshold
        elif num_communities < num_communities_desired_range[0]:
            high = threshold
        else:
            low = threshold
        iteration += 1
    print("Failed to find optimal threshold after", max_iterations, "iterations.")
    return None
