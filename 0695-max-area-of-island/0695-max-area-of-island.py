class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # run dfs only when we find a land
                    maxArea = max(maxArea, self.dfs(grid, i, j))
                    
        return maxArea
    
                    
    def dfs(self, grid, i, j):
		# conditions for out of bound and when we encounter water
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return 0
        
        maxArea = 1
        grid[i][j] = '#'  # this will act as visited set
        maxArea += self.dfs(grid, i+1, j)
        maxArea += self.dfs(grid, i-1, j)
        maxArea += self.dfs(grid, i, j+1)
        maxArea += self.dfs(grid, i, j-1)
        
        return maxArea
#         def inbound(row,col):
#             return 0<=row<len(grid) and 0<=col<len(grid[0])
#         visited=set()
#         directions=[(-1,0),(1,0),(0,1),(0,-1)]
#         y=0
#         def dfs(row,col):
#             visited.add((row,col))
#             for dr,dc in directions:
#                 nr=row+dr
#                 nc=col+dc
#                 if inbound(nr,nc) and (nr,nc)not in visited and grid[nr][nc]==1:
#                     visited.add((nr,nc))
#                     dfs(nr,nc)
#         ans=0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] and (i,j) not in visited:
#                     x=len(visited)
                    
#                     dfs(i,j)
                   
#                     ans=max(len(visited)-x,ans)
#                     y=0
#         return ans