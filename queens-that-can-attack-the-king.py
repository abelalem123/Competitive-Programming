class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens=set(tuple(i) for i in queens)
        arr=[]
        drt=[[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]
        
        for dr,dc in drt:
            r,c=king
            while 0<=r<=7 and 0<=c<=7:
                if(r,c) in queens:
                    arr.append([r,c])
                    break
                r,c= r+dr, c+dc
        return arr
            
