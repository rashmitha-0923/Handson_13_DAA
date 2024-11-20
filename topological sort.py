from collections import defaultdict

class Graph:
    def __init__(self, total_vertices):
        # Initialize the adjacency list to represent the directed graph
        self.adjacency_list = defaultdict(list)
        self.total_vertices = total_vertices

    def add_edge(self, source_node, destination_node):
        # Add a directed edge from 'source_node' to 'destination_node'
        self.adjacency_list[source_node].append(destination_node)

    def topological_sort_helper(self, current_node, visited_nodes, topological_order):
        # Mark the current node as visited
        visited_nodes[current_node] = True

        # Visit all adjacent nodes (dependencies)
        for neighbor_node in self.adjacency_list[current_node]:
            if not visited_nodes[neighbor_node]:
                self.topological_sort_helper(neighbor_node, visited_nodes, topological_order)

        # Insert the current node at the beginning of the topological order list
        topological_order.insert(0, current_node)

    def topological_sort(self, node_list):
        # Create a dictionary to track visited nodes
        visited_nodes = {node: False for node in node_list}
        # List to store the nodes in topological order
        topological_order = []

        # Perform topological sort for each unvisited node
        for node in node_list:
            if not visited_nodes[node]:
                self.topological_sort_helper(node, visited_nodes, topological_order)

        return topological_order

# Define the list of tasks (nodes) for topological sorting
task_nodes = ["undershorts", "pants", "belt", "shirt", "tie", "jacket", "socks", "shoes", "watch"]

# Define the dependencies (edges) as directed relationships between tasks
task_dependencies = [
    ("undershorts", "pants"),
    ("pants", "belt"),
    ("pants", "shoes"),
    ("shirt", "belt"),
    ("shirt", "tie"),
    ("tie", "jacket"),
    ("belt", "jacket"),
    ("socks", "shoes")
]

# Create a Graph instance and add all dependencies (edges)
task_graph = Graph(len(task_nodes))
for start_task, end_task in task_dependencies:
    task_graph.add_edge(start_task, end_task)

# Perform topological sort and print the result
print("Topological Sort Result:", task_graph.topological_sort(task_nodes))
