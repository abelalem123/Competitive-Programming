class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        b-c=> i==len(nums)
        r-r=> var=f(i+1)
        state=>nums[i]
        
        """
        ans=[""]*len(s)
        def rec(s,i):
            if i==len(s)-1:
                return s[-1]
            
            var=rec(s,i+1)
            ans[len(s)-i-2]=var
            # print(var,ans)
            
            return s[i]
        
        rec(s,0)
        ans[-1]=s[0]
        for i in range(len(ans)):
            s[i]=ans[i]
        return ans