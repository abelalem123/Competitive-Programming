class Solution:
    def isPossible(self, nums: List[int]) -> bool:
    
        heap = []
        for i in nums:
          
            while heap and heap[0][0] + 1 < i:
                cur = heappop(heap)
                if cur[1] < 2:
                    return False
            if not heap or heap[0][0] == i:
                heappush(heap, [i, 0])
            else:
                cur = heappop(heap)
                heappush(heap,[i, cur[1] + 1])
        print(heap)
        while heap:
            cur = heappop(heap)
            if cur[1] <2:
                return False
        return True