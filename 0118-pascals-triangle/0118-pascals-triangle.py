class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        def dp(i):
            if i+1>numRows:
                return
            level=[]
            level.append(1)
            for j in range(i-1):
                x=ans[-1][j]+ans[-1][j+1]
                level.append(x)
            level.append(1)
            ans.append(level)
            dp(i+1)
        dp(1)
        return ans