class Solution:
    def combine(self,n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, curr: List[int]):
            if len(curr) == k:
                result.append(curr[:])
                return
            for i in range(start, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()

        result = []
        backtrack(1, [])
        return result