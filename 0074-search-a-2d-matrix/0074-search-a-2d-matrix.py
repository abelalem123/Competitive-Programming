class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1]==target:
                return True
            elif matrix[i][-1]>target:
                if target in matrix[i]:
                    return True
            
        return False
        
#         left=0
#         right=len(matrix)-1
#         row
        
#         while left<=right:
#             mid=(right+left)//2
#             if matrix[mid][-1]<target:
#                 left=mid+1
#             else:
#                 right=mid-1
                
                
        