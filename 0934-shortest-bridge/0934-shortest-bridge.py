class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        visited=set()
        
        def inbound(r,c):
            return 0<=r<n and 0<=c<n
        
        def dfs(r,c):
           
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc]==1:
                    visited.add((nr,nc))
                    dfs(nr,nc)
            
        
        def bfs():
            res,q=0,deque(visited)
            print(q)
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        nr,nc=r+dr,c+dc
                        if not inbound(nr,nc) or (nr,nc) in visited:
                            continue
                        if grid[nr][nc]:
                            return res
                        q.append([nr,nc])
                        visited.add((nr,nc))
                res+=1
            
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    x=bfs()
                    return x
                   
                