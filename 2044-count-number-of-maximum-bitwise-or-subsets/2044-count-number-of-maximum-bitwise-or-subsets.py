class Solution:
    mx=0
    res=0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        for num in nums:
            self.mx|=num
        self.back(nums,0,0)
        return self.res
    def back(self,nums,start,val):
        if val==self.mx:
            self.res+=1
        for i in range(start,len(nums)):
            self.back(nums,i+1,val|nums[i])