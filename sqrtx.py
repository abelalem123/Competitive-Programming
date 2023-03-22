class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        if x==0:
            return 0
        """
        0 1 2 3 4 5 6 7 8
            ^ ^
        """
        while l<=r:
            m=l+(r-l)//2
            p=m*m
            if p>x:
                r=m-1
            else:
                l=m+1
            
        return r
