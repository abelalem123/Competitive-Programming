class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        ans=""
        length=max(len(word1),len(word2))
        while i<length and j<length:
            if i<len(word1):
                ans=ans+word1[i]
                i+=1
            if j<len(word2):
                ans=ans+word2[j]
                j+=1
        return ans
