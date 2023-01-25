class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        dirs=[(0,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,0),(1,1)]
        max_hour=0
        for row in range(1,rows-1):
            for col in range(1,cols-1):
                cur_hour = 0
                for dy,dx in dirs:
                    cur_hour+=grid[row+dy][col+dx]
                max_hour=max(max_hour,cur_hour)
        return max_hour  