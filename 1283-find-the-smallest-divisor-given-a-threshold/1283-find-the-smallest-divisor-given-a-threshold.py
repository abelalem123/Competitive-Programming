class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r=1,max(nums)
        while l<r:
            mid=l+(r-l)//2
            total=sum([ceil(i/mid) for i in nums])
            if total>threshold:
                l=mid+1
            else:
                r=mid
        return l