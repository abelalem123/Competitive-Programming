class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def dp(i):
            if i>=len(cost):
                return 0
            if i in memo:
                return memo[i]
            res=min(dp(i+1),dp(i+2))+cost[i]
            
            memo[i]=res
            return res
        return min(dp(0),dp(1))