class Solution:
    def minSwaps(self, s: str) -> int:
        l=0
        r=0
        for i in s:
            if i==']':
                r+=1
            else:
                r-=1
            l=max(l,r)
        
        return (l+1)//2