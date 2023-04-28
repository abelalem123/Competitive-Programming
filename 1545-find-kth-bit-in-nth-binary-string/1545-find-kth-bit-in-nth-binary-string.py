class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x=self.rec(n,'0',0)
        return x[k-1]
    def rec(self,n,s,num):
        if n==num:
            return s
        if n==1:
            return '0'
        
        inv = ''.join(['1' if i == '0' else '0'
                     for i in s])
        sr=s+'1'+inv[::-1]
        x=self.rec(n,sr,num+1)
        return x