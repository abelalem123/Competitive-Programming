class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, n):
            if n == 0:
                return 1
            
            ans = power(x, n//2)
            ans = ans*ans%(10**9+7)
            
            if n%2:
                return ans*x
            else:
                return ans
        if n%2:
            e = n//2+1
            o = n//2
        else:
            e = n//2
            o = n//2
            
        return (power(5, e)*power(4, o))%(10**9+7)
