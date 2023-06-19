class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        nums=[0]*(n+1)
        for i in range(n):
            nums[i+1]=nums[i]+gain[i]
        return max(nums)