class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=[]
        while l<r:
            ans.append(nums[l])
            ans.append(nums[r])
            l+=1
            r-=1
        if len(ans)<len(nums):  
            ans.append(nums[l]);
        return ans