class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        
        i,j=0,0
        
        while j<len(nums):
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            elif nums[i]!=0:
                i+=1
            
            j+=1
        
        return nums
