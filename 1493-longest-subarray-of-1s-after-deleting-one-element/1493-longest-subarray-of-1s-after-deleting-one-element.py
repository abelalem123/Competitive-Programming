class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        l=0
        r=0
        ans=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
            while zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            ans=max(ans,r-l)
            r+=1
            
        return ans