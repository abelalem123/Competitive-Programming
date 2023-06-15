class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        [4,12,2,7,3,18,20,3,19] b=2 l=1
        """
        n=len(heights)
        heap=[]
        for i in range(n-1):
            diff=heights[i+1]-heights[i]
            if diff>0:
                heapq.heappush(heap,diff)
                if len(heap)>ladders:
                    bricks-=heapq.heappop(heap)
                if bricks<0:
                    return i
        return n-1