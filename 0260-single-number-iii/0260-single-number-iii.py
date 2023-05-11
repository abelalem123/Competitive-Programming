class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for num in nums:
            x^=num
        diff=x&-x
        g1=0
        g2=0
        for num in nums:
            if num&diff==0:
                g1^=num
            else:
                g2^=num
        return [g1,g2]