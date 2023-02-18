class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        r=floor(sqrt(c))
        l=0
        while l<=r:
            
            res=l**2+r**2
            if res==c:
                return True
            elif res>c:
                r-=1
            else:
                l+=1
        
        return False
    
    
