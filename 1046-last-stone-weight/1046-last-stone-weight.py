class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        p=[-i for i in stones]
        heapq.heapify(p)
        while len(p)>1:
            x=-1*(heapq.heappop(p))
            y=-1*(heapq.heappop(p))
            if x==y:
                continue
            heapq.heappush(p,y-x)
        ans=0
        if p:
            ans=-1*(heapq.heappop(p))
        return ans
            
        