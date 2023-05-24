class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))
        visited = [[False for i in range(len(mat[0]))] for j in range(len(mat))]

        queue = collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    visited[i][j]=True
                    queue.append([i,j,0])
        while queue:
            r,c,count = queue.popleft()
            for rn,cn in directions:
                new_row=r+rn
                new_col=c+cn
                if inbound(new_row,new_col) and visited[new_row][new_col]==False:
                    visited[new_row][new_col]=True
                    queue.append([new_row,new_col,count+1])
                    ans[new_row][new_col]=count+1
            
        return ans
