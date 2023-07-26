class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            res=max(dp(i+2),dp(i+3))+nums[i]
            
            memo[i]=res
            return res
        return max(dp(0),dp(1))