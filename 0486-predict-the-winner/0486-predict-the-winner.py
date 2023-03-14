class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=1000)
        def take(turn,i,j):
            if i==j:
                return turn * nums[i] 

            choice_i= turn * nums[i] + take(-turn,i+1,j)
            choice_j= turn * nums[j] + take(-turn,i,j-1)
            if turn==1:
                return max(choice_i,choice_j)
            return min(choice_i,choice_j)
        
           # return turn * max(turn *choice_i,turn*choice_j)
        ans = take(1,0,len(nums)-1)
        return ans >= 0