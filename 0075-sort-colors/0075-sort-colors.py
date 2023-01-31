class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)):
            for i in range(1,len(nums)-j):
                if nums[i-1]>nums[i]:
                    temp=nums[i-1]
                    nums[i-1]=nums[i]
                    nums[i]=temp
            
            