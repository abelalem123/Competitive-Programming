class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set((0,0))
        q=deque([(0,0,1)])
        directions=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        while q:
            r,c,length=q.popleft()
            if (min(r,c)<0 or max(r,c)>=n or grid[r][c]):
                continue
            if r==n-1 and c==n-1:
                return length
            for dr,dc in directions:
                if (r+dr,c+dc) not in visited:
                    q.append((r+dr,c+dc,length+1))
                    visited.add((r+dr,c+dc))
                
        return -1
             