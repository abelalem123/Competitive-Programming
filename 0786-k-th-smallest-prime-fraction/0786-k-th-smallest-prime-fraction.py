class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                heapq.heappush(heap,[arr[i]/arr[j],arr[i],arr[j]])
        x=0
        for _ in range(k):
            x=heapq.heappop(heap)
        return [x[1],x[2]]