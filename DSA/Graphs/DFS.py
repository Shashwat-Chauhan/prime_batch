def dfs(adj_list, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')  # Visit the node

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited)

# Example usage
adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:")
dfs(adj_list, 'A')



