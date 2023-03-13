class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n==0 or n%4!=0:
            return False
        return Solution.isPowerOfFour(self,n//4)
        