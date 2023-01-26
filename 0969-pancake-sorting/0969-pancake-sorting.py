class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1, -1, -1):
            minIndex = i
            for j in range(i-1, -1, -1):
                if arr[j] < arr[minIndex]:
                    minIndex = j

            if minIndex != i:
                arr = list(reversed(arr[:minIndex+1])) + arr[minIndex+1:]
                arr = list(reversed(arr[:i+1])) + arr[i+1:]
                res.extend([minIndex+1, i+1])

        res.append(len(arr))
        return res