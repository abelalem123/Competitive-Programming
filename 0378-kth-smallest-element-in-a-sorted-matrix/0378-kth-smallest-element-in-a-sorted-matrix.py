class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in matrix:
            heap.extend(i)
        heapq.heapify(heap)
        x=heap[0]
        for _ in range(k):
            x=heapq.heappop(heap)
        return x