adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(node , graph , visited):
    print(node , end= ' ')
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour , graph , visited)


visited = set()
print("DFS Traversal:")
dfs('A', adj_list, visited)



