class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        total=set()
        sub=[]
        nums=sorted(nums)
        def dfs(i):
            if i>=len(nums):
                total.add(' '.join(sub.copy()))
                return
            
            sub.append(str(nums[i]))
            dfs(i+1)
            sub.pop()
            dfs(i+1)
       
        dfs(0)
        print(total)
        ans=[]
        for i in total:
            x=list(map(int,i.split()))
            ans.append(x)
        return ans