def getAns(mat: list[list] , row: int , col:int , path: str, ans ,  vis: list[list[bool]]):
    n = len(mat)
    if (row < 0 or col < 0 or row >= n or col >= n or mat[row][col] == 0 or vis[row][col] == True ):
        return 
    
    if row == n-1 and col == n-1:
        ans.append(path)
        return

    vis[row][col] = True
    
    getAns(mat , row+1 , col , path+"D" , ans , vis) #Down Call
    getAns(mat , row-1 , col , path+"U" , ans , vis) #Up Call
    getAns(mat , row , col+1 , path+"R" , ans , vis) #Right Call
    getAns(mat , row , col-1 , path+"L" , ans , vis) #Left Call

    vis[row][col] = False
 

vis = [[False for _ in range(4)] for _ in range(4)]
matrix = [[1, 0, 0, 0] , [1, 1, 0, 1] , [1, 1, 0, 0] , [0, 1, 1, 1]]
path = ""
ans = []
getAns(matrix, 0, 0, path, ans , vis)
print(ans)
