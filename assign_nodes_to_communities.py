# Assign nodes to communities based on gravity threshold
def assign_nodes_to_communities(G, threshold):
    MaxGravityTable = calculate_max_gravity_table(calculate_gravity_table(G))
    CommunityTable = {}
    community_number = 1
    for node, (gravity, pair_node) in MaxGravityTable.items():
        if gravity is not None and gravity > threshold:
            if node not in CommunityTable:
                CommunityTable[node] = community_number
            if pair_node not in CommunityTable:
                CommunityTable[pair_node] = community_number
            community_number += 1
        elif node not in CommunityTable:
            CommunityTable[node] = community_number
    return CommunityTable
