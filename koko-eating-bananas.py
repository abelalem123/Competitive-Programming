class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s=sum(piles)
        l=1
        r=max(piles)
        
        while  l<r:
            mid=l+(r-l)//2
            count=0
            for x in piles:
                if mid>=x:
                    count+=1
                else:
                    c=ceil(x/mid)
                    count+=c

            if count<=h:
                r=mid
            else:
                l=mid+1
        return l
