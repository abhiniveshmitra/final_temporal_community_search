# Calculate max gravity table
def calculate_max_gravity_table(GravityTable):
    MaxGravityTable = {}
    for entry in GravityTable:
        node1, node2, gravity = entry
        if node1 not in MaxGravityTable:
            MaxGravityTable[node1] = (gravity, node2)
        else:
            if gravity > MaxGravityTable[node1][0]:
                MaxGravityTable[node1] = (gravity, node2)
        if node2 not in MaxGravityTable:
            MaxGravityTable[node2] = (gravity, node1)
        else:
            if gravity > MaxGravityTable[node2][0]:
                MaxGravityTable[node2] = (gravity, node1)
    return MaxGravityTable
