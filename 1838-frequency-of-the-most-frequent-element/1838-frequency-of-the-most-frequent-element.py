class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        totalSum=0
        ans=0
        
        for i,r in enumerate(nums):
            totalSum+=r
            while r*(i-l+1)>totalSum+k:
                
                totalSum-=nums[l]
                l+=1
            
            ans=max(ans,i-l+1)
        return ans
            
