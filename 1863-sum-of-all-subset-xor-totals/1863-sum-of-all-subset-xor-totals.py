class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=[]
        sub=[]
        def dfs(i):
            if i>=len(nums):
                total.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        ans=0
        for i in total:
            if len(i)>0:
                s=i[0]
                
                for j in range(1,len(i)):
                    s^=i[j]
                ans+=s
        return ans