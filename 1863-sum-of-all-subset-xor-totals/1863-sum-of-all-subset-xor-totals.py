class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=[]
        sub=[]
        def dfs(i):
            if i>=len(nums):
                if sub:
                    total.append(reduce(lambda a, b: a^b, sub))
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        
        return sum(total)