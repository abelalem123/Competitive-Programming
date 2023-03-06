class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        s1=sum(nums[l:r])
        m=s1/k
        while r<len(nums):
            s1=s1+nums[r]-nums[l]
            m=max(m,s1/k)
            l+=1
            r+=1
        return m
            
        