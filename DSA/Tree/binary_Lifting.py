import sys
import math
sys.setrecursionlimit(2 * 10**5)

n = 0  # set this before calling preprocess
l = 0
adj = []

timer = 0
tin = []
tout = []
up = []

def dfs(v, p):
    global timer
    tin[v] = timer
    timer += 1
    up[v][0] = p
    for i in range(1, l + 1):
        up[v][i] = up[up[v][i - 1]][i - 1]

    for u in adj[v]:
        if u != p:
            dfs(u, v)

    tout[v] = timer
    timer += 1

def is_ancestor(u, v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]

def lca(u, v):
    if is_ancestor(u, v):
        return u
    if is_ancestor(v, u):
        return v
    for i in range(l, -1, -1):
        if not is_ancestor(up[u][i], v):
            u = up[u][i]
    return up[u][0]

def preprocess(root):
    global tin, tout, timer, l, up
    l = math.ceil(math.log2(n))
    tin = [0] * n
    tout = [0] * n
    up = [[0] * (l + 1) for _ in range(n)]
    timer = 0
    dfs(root, root)
