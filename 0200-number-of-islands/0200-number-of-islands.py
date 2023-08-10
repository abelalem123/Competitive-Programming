class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        [["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]
        """
        visited=set()
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        def dfs(row,col):
            visited.add((row,col))
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc]=='1':
                    visited.add((nr,nc))
                    dfs(nr,nc)
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    
                    dfs(i,j) 
                    ans+=1
        return ans
            