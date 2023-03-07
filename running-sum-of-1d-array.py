class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=nums[0]
        for i in range(1,len(nums)):
            s=s+nums[i]
            nums[i]=s
        return nums
