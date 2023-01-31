class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])): 
            for j in range(1,len(strs)):
                if ord(strs[j-1][i])>ord(strs[j][i]):
                    count+=1
                    break
            
        return count
