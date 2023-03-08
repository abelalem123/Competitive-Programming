class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicts={}
        dicts[0]=1
        s=0
        count=0
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in dicts:
                count+=dicts[s-k]
            if s in dicts:
                dicts[s]+=1
            else:
                dicts[s]=1
        return count