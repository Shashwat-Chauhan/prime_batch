graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'] 
}


def bfs(graph , start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node , end =  ' ')
            visited.add(node)


        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    return

bfs(graph , 'A')


