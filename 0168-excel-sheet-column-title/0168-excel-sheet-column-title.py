class Solution:
    def convertToTitle(self, columnNumber):
        ans = []
        
        while columnNumber > 0:
            columnNumber -= 1
            
            ans.append(chr((columnNumber) % 26 + ord('A')))
            columnNumber = (columnNumber) // 26
        
    
        return ''.join(ans[::-1])