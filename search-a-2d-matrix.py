class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1]==target:
                return True
            elif matrix[i][-1]>target:
                if target in matrix[i]:
                    return True
            
        return False
