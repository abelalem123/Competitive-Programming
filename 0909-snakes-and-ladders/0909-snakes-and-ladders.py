class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        board.reverse()
        
        def intToPos(num):
            r=(num-1)//n
            c=(num-1)%n
            if r%2:
                c=n-1-c
            return [r,c]
        q=deque()
        q.append([1,0])
        visited=set()
        
        while q:
            num,count=q.popleft()
            for i in range(1,7):
                nextNum=num+i
                r,c = intToPos(nextNum)
                if board[r][c]!= -1:
                    nextNum=board[r][c]
                if nextNum==n*n:
                    return count+1
                if nextNum not in visited:
                    q.append([nextNum,count+1])
                    visited.add(nextNum)
        return -1