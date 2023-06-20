class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        if len(nums)<2*k:
            return [-1]*len(nums)
        for i in range(len(nums)-1):
            nums[i+1]=nums[i]+nums[i+1]
        ans=[-1]*len(nums)
        c=k
        l=c-k
        r=c+k
        while r<len(nums):
            if l>0:
                s=nums[r]-nums[l-1]
            else:
                s=nums[r]
            a=s//(r-l+1)
            ans[c]=a
            c+=1
            l+=1
            r+=1
        return ans
    
                
            