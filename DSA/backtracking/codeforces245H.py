print("Enter:")
s = input()
T = int(input())
n = len(s)
l = [[1]*n for i in range(n)]

for i in range(T):
    i, j = map(int , input().split())
    
