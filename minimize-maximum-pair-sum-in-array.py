class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum=0
        l=0
        r=len(nums)-1
        nums.sort()
        while l<r:
            max_sum=max(max_sum,nums[l]+nums[r])
            l+=1
            r-=1
        return max_sum
            
