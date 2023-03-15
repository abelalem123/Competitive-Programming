class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def rec(turn,l,r):
            #p1 postive
            if l==r:
                return turn*nums[l]
            left=turn*nums[l]+rec(-turn,l+1,r)
            right=turn*nums[r]+rec(-turn,l,r-1)
            
            if turn==1:
                return max(left,right)
            else:
                return min(left,right)
        res=rec(1,0,len(nums)-1)
        return res>=0
