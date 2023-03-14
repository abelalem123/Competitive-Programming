class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: 
            return [1]
        prevrow = self.getRow(rowIndex-1)
        print(prevrow,rowIndex)
        res = [1]
        for i in range(1, rowIndex):
            res.append(prevrow[i-1]+prevrow[i])
        res.append(1)
        return res