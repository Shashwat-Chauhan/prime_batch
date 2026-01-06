edges = [(0,1), (0,2), (1,3), (2,3)]
n = 4

adj_matrix = [[0] * n for i in range(n)]


for u , v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

for row in adj_matrix:
    print(row)