class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count=0
        max_num=0
        for i in range(len(arr)):
            max_num=max(max_num,arr[i])
            if max_num==i:
                print(max_num,i)
                count+=1
        return count