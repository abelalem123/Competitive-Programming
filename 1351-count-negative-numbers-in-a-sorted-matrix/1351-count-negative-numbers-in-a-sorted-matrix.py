class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        row_len=len(grid[0])
        col_len=len(grid)
        
        i=0
        j=row_len-1
        
        ans=0
        while i<col_len and j>=0:
            if grid[i][j]<0:
                ans+=col_len-i
                j-=1
            else:
                i+=1
        return ans
                