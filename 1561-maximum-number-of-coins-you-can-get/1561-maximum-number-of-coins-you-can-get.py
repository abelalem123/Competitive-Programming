class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        r=len(piles)-1
        s=0
        while(r-1>l):
            s+=piles[r-1]
            l+=1
            r-=2
        return s
        
        