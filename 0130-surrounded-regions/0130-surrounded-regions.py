class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        [["X","O","X","O","X","O"],
        ["O","X","O","X","O","X"],
        ["X","O","X","O","X","O"],
        ["O","X","O","X","O","X"]]
        """
        n=len(board)
        m=len(board[0])
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        visited=set()
        def inbound(row,col):
            return 0<=row<len(board) and 0<=col<len(board[0])
        def dfs(row,col):
            board[row][col]='T'
            for dr,dc in directions:
                nr=dr+row
                nc=dc+col
                if inbound(nr,nc) and (nr,nc) not in visited and board[nr][nc]=='O' :
                    visited.add((nr,nc))
                    dfs(nr,nc)
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if board[i][j]=="O":
                        dfs(i,j)
                        
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='T':
                    board[i][j]='O'
         
                
      
        