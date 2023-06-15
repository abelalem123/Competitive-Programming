class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums=[-i for i in piles]
        heapq.heapify(nums)
        
        for _ in range(k):
            x=heapq.heappop(nums)
            heapq.heappush(nums,ceil(x//2))
        s=0
        for i in nums:
            s+=i
        return -s