from collections import defaultdict

def depth_first_search(edge_list, start_node):
    # Create an adjacency list to represent the graph
    adjacency_list = defaultdict(list)
    for source, destination in edge_list:
        adjacency_list[source].append(destination)

    # Set to keep track of visited nodes
    visited_nodes = set()

    # Helper function to perform DFS recursively
    def dfs_recursive(node):
        if node not in visited_nodes:
            # Print the current node and mark it as visited
            print(node, end=' ')
            visited_nodes.add(node)
            # Visit all adjacent nodes
            for adjacent_node in adjacency_list[node]:
                dfs_recursive(adjacent_node)

    # Start DFS from the given start node
    dfs_recursive(start_node)
    print()  # Print a newline after DFS completes

# Define the list of directed edges for the DFS example
graph_edges = [
    ("node_u", "node_v"),
    ("node_u", "node_x"),
    ("node_v", "node_y"),
    ("node_y", "node_x"),
    ("node_x", "node_v"),
    ("node_w", "node_z"),
    ("node_w", "node_y"),
    ("node_z", "node_z")  # Self-loop for demonstration
]

# Run DFS starting from 'node_u' and print the result
print("Depth-First Search starting from 'node_u':")
depth_first_search(graph_edges, 'node_u')
