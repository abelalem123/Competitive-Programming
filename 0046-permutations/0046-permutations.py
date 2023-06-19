class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        total=[] 
        def dfs(path,numss):
            if path and  len(path)==len(nums):
                
                total.append(path)
                return
            for i in range(len(numss)):
                dfs(path+[numss[i]],numss[:i]+numss[i+1:])
        dfs([],nums)
        return total