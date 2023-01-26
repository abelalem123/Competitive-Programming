class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        dicts={}
        
        for i,num in enumerate(temp):
            if num not in dicts:
                dicts[num]=i
                
        res=[dicts[i] for i in nums]
        return res
        