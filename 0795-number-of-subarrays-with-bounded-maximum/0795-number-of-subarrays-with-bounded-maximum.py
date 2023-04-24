class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
   
        count = 0
        left_bound = -1
        right_bound = -1
        for i in range(len(nums)):
            if nums[i] > right:
                left_bound = i
            if nums[i] >= left:
                right_bound = i
            count += right_bound - left_bound
        return count