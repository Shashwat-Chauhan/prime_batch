grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]      

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid[0])
        visited_matrix = [[0] * n for i in range(len(grid))]
        

        def bfs(r , c , visited_matrix , grid):
            queue = []
            visited_matrix[r][c] = 1
            n = len(grid)
            m = len(grid[0])
            queue.append([r , c])


            while(queue):
                node = queue.pop(0)
                r = node[0]
                c = node[1]

                for delrow in range(-1 , 2 , 1 ):
                    for delcol in range(-1 , 2 , 1):
                        nrow = r + delrow
                        ncol = c + delcol

                        if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m) and grid[nrow][ncol] == "1" and visited_matrix[nrow][ncol] == 0:
                            visited_matrix[nrow][ncol] = 1
                            queue.append([nrow , ncol])



        count = 0
        for i in range(len(grid)):
            for j in range(n):
                if visited_matrix[i][j] == 0 and grid[i][j] == "1":
                    count += 1
                    bfs(i , j , visited_matrix , grid)
z   

        return count

s = Solution()

ans = s.numIslands(grid)
print(ans)


