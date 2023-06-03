class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        visited=set()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        y=0
        def dfs(row,col):
            visited.add((row,col))
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if inbound(nr,nc) and (nr,nc)not in visited and grid[nr][nc]==1:
                    visited.add((nr,nc))
                    dfs(nr,nc)
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    x=len(visited)
                    
                    dfs(i,j)
                   
                    ans=max(len(visited)-x,ans)
                    y=0
        return ans