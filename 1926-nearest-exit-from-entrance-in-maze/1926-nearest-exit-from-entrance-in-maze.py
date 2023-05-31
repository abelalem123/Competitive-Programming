class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        
        def inbound(row,col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])
        
        while q:
            r,c,count=q.popleft()
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and (r, c) != (entrance[0], entrance[1]):
                return count
    
            
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if inbound(nr,nc) and (nr,nc) not in visited and maze[nr][nc]=='.':
                    visited.add((nr, nc))
                    q.append((nr, nc, count+1))
        return -1
            