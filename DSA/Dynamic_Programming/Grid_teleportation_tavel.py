from typing import List
from collections import defaultdict, deque

class Solution:
    def minMoves(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Collect portal positions
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if 'A' <= ch <= 'Z':
                    portals[ch].append((i, j))
        
        # Step 2: BFS using proper deque for efficiency
        queue = deque([(0, 0, 0)])  # (x, y, moves)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        # Track portals used in each path
        portal_states = {(0, 0): set()}  # (x, y): set of used portals
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, moves = queue.popleft()
            
            # Check if we've reached the destination
            if (x, y) == (m - 1, n - 1):
                return moves
                
            cell = matrix[x][y]
            used_portals = portal_states.get((x, y), set())
            
            # Use teleportation if applicable and we haven't used this portal yet
            if 'A' <= cell <= 'Z' and cell not in used_portals:
                for nx, ny in portals[cell]:
                    if (nx, ny) != (x, y):  # Don't teleport to same location
                        new_portals = used_portals.copy()
                        new_portals.add(cell)
                        
                        # If we haven't visited this position or we have a new portal state
                        new_state = (nx, ny, frozenset(new_portals))
                        if not visited[nx][ny] or (nx, ny) not in portal_states or new_portals != portal_states[(nx, ny)]:
                            visited[nx][ny] = True
                            portal_states[(nx, ny)] = new_portals
                            # Teleportation doesn't count as a move
                            queue.appendleft((nx, ny, moves))
            
            # Try moving in 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if matrix[nx][ny] != '#':
                        visited[nx][ny] = True
                        portal_states[(nx, ny)] = used_portals.copy()
                        queue.append((nx, ny, moves + 1))
        
        return -1