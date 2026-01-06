# #There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Above graph looks like this
#    1-----2

#       3






def findCircleNum(isConnected):
    def dfs(node , adj_matrix ,  visited):

        visited.add(node)

        for neighbour in range(len(adj_matrix)):
            if adj_matrix[node][neighbour] == 1 and neighbour not in visited:
                dfs(neighbour , adj_matrix , visited)
        
    n = len(isConnected)
    visited = set()
    
    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i , isConnected , visited)
            count += 1
    
    return count 



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
ans = findCircleNum(isConnected)
print(ans)