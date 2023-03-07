class NumArray:

    def __init__(self, nums: List[int]):
    
        s=nums[0]
        for i in range(1,len(nums)):
            s+=nums[i]
            nums[i]=s
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.nums[right]
        else:
            return self.nums[right]-self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)