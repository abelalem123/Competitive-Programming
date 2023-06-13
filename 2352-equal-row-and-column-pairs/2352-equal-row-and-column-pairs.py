class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m=defaultdict(int)
        count=0
        for row in grid:
            m[str(row)]+=1
        for i in range(len(grid[0])):
            temp=[]
            for j in range(len(grid)):
                temp.append(grid[j][i])
            count+=m[str(temp)]
        return count