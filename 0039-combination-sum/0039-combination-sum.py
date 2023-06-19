class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total=[]
        sub=[]
        
        def dfs(i):
            if sum(sub)==target:
                total.append(sub.copy())
                return
            if i>=len(candidates) or sum(sub)>target:
                return
            sub.append(candidates[i])
            dfs(i)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return total
                