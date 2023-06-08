class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        p=[-i for i in stones]
        
        while len(p)>1:
            heapq.heapify(p)
            x=-1*(heapq.heappop(p))
            y=-1*(heapq.heappop(p))
            if x==y:
                continue
            heapq.heappush(p,y-x)
        ans=0
        if p:
            ans=-1*(heapq.heappop(p))
        return ans
            
        