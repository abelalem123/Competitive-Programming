class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        for i in nums:
            count[i]+=1
        res=[]
        
        for i in nums:
            res.append(sum(count[:i]))
        return res
    
#         temp=sorted(nums)
#         dicts={}
        
#         for i,num in enumerate(temp):
#             if num not in dicts:
#                 dicts[num]=i
                
#         res=[dicts[i] for i in nums]
#         return res

        