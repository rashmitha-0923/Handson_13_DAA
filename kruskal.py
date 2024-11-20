class Edge:
    def __init__(self, weight, start_node, end_node):
        self.weight = weight
        self.start_node = start_node
        self.end_node = end_node

class UnionFind:
    def __init__(self, elements):
        # Initialize the parent dictionary where each element points to itself
        self.parent_map = {element: element for element in elements}
        # Initialize the rank dictionary to track the depth of trees
        self.rank_map = {element: 0 for element in elements}

    def find(self, element):
        # Path compression for optimization, making the tree flatter
        if self.parent_map[element] != element:
            self.parent_map[element] = self.find(self.parent_map[element])
        return self.parent_map[element]

    def union(self, element1, element2):
        # Find the roots of the elements
        root1 = self.find(element1)
        root2 = self.find(element2)
        # Union by rank to maintain a balanced tree structure
        if root1 != root2:
            if self.rank_map[root1] > self.rank_map[root2]:
                self.parent_map[root2] = root1
            elif self.rank_map[root1] < self.rank_map[root2]:
                self.parent_map[root1] = root2
            else:
                self.parent_map[root2] = root1
                self.rank_map[root1] += 1

def kruskal(node_set, edge_list):
    # Sort the edges by weight in non-decreasing order
    sorted_edges = sorted(edge_list, key=lambda edge: edge.weight)
    # Initialize the Union-Find structure with the given nodes
    uf = UnionFind(node_set)
    # List to store the edges that will form the minimum spanning tree (MST)
    mst_edges = []

    for edge in sorted_edges:
        # Check if adding this edge creates a cycle
        if uf.find(edge.start_node) != uf.find(edge.end_node):
            # Union the nodes and add the edge to the MST
            uf.union(edge.start_node, edge.end_node)
            mst_edges.append(edge)

    return mst_edges

# Define the set of nodes and the list of edges for Kruskal's algorithm
nodes_set = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
edges_list = [
    Edge(4, "a", "b"),
    Edge(8, "a", "h"),
    Edge(8, "b", "c"),
    Edge(11, "b", "h"),
    Edge(7, "c", "d"),
    Edge(4, "c", "f"),
    Edge(2, "c", "i"),
    Edge(6, "c", "g"),
    Edge(9, "d", "e"),
    Edge(14, "d", "f"),
    Edge(10, "e", "f"),
    Edge(2, "f", "g"),
    Edge(1, "g", "h"),
    Edge(7, "h", "i")
]

# Execute Kruskal's algorithm to find the MST
mst_result = kruskal(nodes_set, edges_list)
print("Kruskal's MST:")
for edge in mst_result:
    print(f"Edge {edge.start_node}-{edge.end_node} with weight {edge.weight}")
