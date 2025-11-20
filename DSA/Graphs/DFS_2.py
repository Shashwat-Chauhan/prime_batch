def dfs(node, adj_matrix, visited):
    visited[node] = True
    print(node, end=' ')
    
    for neighbor in range(len(adj_matrix)):
        if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, adj_matrix, visited)

# Example adjacency matrix for 6 nodes (0 to 5)
adj_matrix = [
    #0 1 2 3 4 5
    [0,1,1,0,0,0],  # 0
    [1,0,0,1,1,0],  # 1
    [1,0,0,0,0,1],  # 2
    [0,1,0,0,0,0],  # 3
    [0,1,0,0,0,1],  # 4
    [0,0,1,0,1,0],  # 5
]

n = len(adj_matrix)
visited = [False] * n

print("DFS Traversal starting from node 0:")
dfs(0, adj_matrix, visited)
