class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=[[False for i in range(len(image[0]))] for i in range(len(image))]
        def inbound(row,col):
            return 0<=row<len(image) and 0<=col<len(image[0])
        val=image[sr][sc]
        def dfs(row,col):
            nonlocal val
            visited[row][col]=True
           
            image[row][col]=color            
            for r,c in directions:
                new_row=row+r
                new_col=col+c
                
                if inbound(new_row,new_col) and not visited[new_row][new_col] and image[new_row][new_col]==val:
                    dfs(new_row,new_col)
                    
        dfs(sr,sc)
        return image