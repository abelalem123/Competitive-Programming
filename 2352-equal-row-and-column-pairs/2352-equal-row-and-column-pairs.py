class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
      
        count=0
        for lst in grid:
            for i in range(len(grid[0])):
                temp=[]
                for j in range(len(grid)):
                    temp.append(grid[j][i])
                if lst==temp:
                    count+=1
        return count