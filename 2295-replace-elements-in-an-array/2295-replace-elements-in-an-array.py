class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {n: i for i,n in enumerate(nums)}
        results = nums

        for o in operations:
            d[o[1]] = d[o[0]]
            results[d[o[0]]] = o[1]

            del d[o[0]]

        return results